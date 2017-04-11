import re

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
        super(AbstractBase, self).save(*args, **kwargs)


class Base(AbstractBase):

    class Meta:
        abstract = True


class Slugged(models.Model):
    """
    Comment goes here
    """
    slug = models.SlugField(db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.name.isalnum():
            self.slug = self.name.lower()[:50]
        else:
            name = '-'.join(self.name.lower()[:50].split())
            self.slug = re.sub("[^a-z0-9\-]+", "", name)

        super(Slugged, self).save(*args, **kwargs)
