import os
import stat
import subprocess
import time

from django.contrib.staticfiles.management.commands.collectstatic import (
        Command as CollectstaticCommand)
from django.conf import settings


class Command(CollectstaticCommand):

    def handle(self, **options):
        BASE_DIR = settings.BASE_DIR
        STATIC_DIR = os.path.join(BASE_DIR, 'static')

        self.status_filename = os.path.join(BASE_DIR, '.modified')

        first_run = False

        if os.path.isfile(self.status_filename):
            with open(self.status_filename, 'r') as f:
                etime = int(f.read())
        else:
            first_run = True

        for root, dirs, files in os.walk(STATIC_DIR):
            for _file in files:
                if _file.endswith('styl'):
                    current_file = os.path.join(root, _file)
                    last_modified = os.stat(current_file)[stat.ST_MTIME]
                    if first_run or last_modified >= etime:
                        subprocess.run([
                            'stylus', current_file, '--out', root])

        super(Command, self).handle(**options)

        self.save_status()

    def save_status(self):
        with open(self.status_filename, 'w') as f:
            f.write(str(int(time.time())))
