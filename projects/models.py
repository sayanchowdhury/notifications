from django.db import models

from app.core.models import Base


class Project(Base):
    """
    Comment goes here.
    """
    name = models.CharField(max_length=255, db_index=True)
