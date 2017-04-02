from django.urls import reverse

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class NotificationsSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Comment goes here
    """
    def get_connect_redirect_url(self, request, socialaccount):
        if request.user.is_authenticated():
            return reverse('profiles_dashboard', args=[request.user.username])
