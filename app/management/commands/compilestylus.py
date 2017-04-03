import os
import subprocess

from os.path import getmtime

from django.contrib.staticfiles.management.commands.collectstatic import (
        Command as CollectstaticCommand)
from django.conf import settings


class Command(CollectstaticCommand):

    def handle(self, **options):
        BASE_DIR = settings.BASE_DIR
        STATIC_DIR = os.path.join(BASE_DIR, 'static')

        all_stylus_files = []

        for cur, _dir, files in os.walk(STATIC_DIR):
            for _file in files:
                if _file.endswith('.styl'):
                    filename = '/'.join([cur, _file])
                    all_stylus_files.append(filename)

        for stylus_filename in all_stylus_files:
            css_filename = stylus_filename.replace('.styl', '.css')

            if not os.path.isfile(css_filename):
                print('Processing ', stylus_filename)
                subprocess.run([
                    'stylus', stylus_filename, '--out', css_filename])

            if getmtime(stylus_filename) > getmtime(css_filename):
                print('Processing ', stylus_filename)
                subprocess.run([
                    'stylus', stylus_filename, '--out', css_filename])

        super(Command, self).handle(**options)
