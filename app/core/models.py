from datetime import datetime

from django.db import models


class AbstractBase(models.Model):
    """
    Comment goes here.
    """
    timestamp = models.DateTimeField(blank=True, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = datetime.now()


class Base(AbstractBase):

    class Meta:
        abstract = True
