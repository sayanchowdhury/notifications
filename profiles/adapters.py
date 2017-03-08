from django.urls import reverse

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Comment goes here
    """
    def get_login_redirect_url(self, request):
        if request.user.is_authenticated():
            return reverse('profiles_dashboard', args=[request.user.username])
