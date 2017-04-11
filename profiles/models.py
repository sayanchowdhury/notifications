import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse

from app.core.models import Base


class Profile(Base):
    """
    Comment goes here.
    """
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    last_logged_in = models.DateTimeField(db_index=True)

    def get_absolute_url(self):
        return reverse('profiles_dashboard', args=[self.user.username])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            last_logged_in=datetime.datetime.utcnow(),
        )
        profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
