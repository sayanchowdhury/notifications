from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.core.models import Base


class UserProfile(Base):
    """
    Comment goes here.
    """
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    last_logged_in = models.DateTimeField(db_index=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
