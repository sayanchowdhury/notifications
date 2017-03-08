from django.db import models

from app.core.models import Base


class UserProfile(Base):
    """
    Comment goes here.
    """

    last_logged_in = models.DateTimeField(db_index=True)
