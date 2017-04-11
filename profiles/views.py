import json

from django.shortcuts import render

from profiles.models import Profile


def dashboard(request, username, param1=None):
    """
    Comment goes here
    """
    template = 'profiles/dashboard.html'
    history = []

    if param1 is None:
        param1 = 'dashboard'
    history.append(param1)

    profile = Profile.objects.get(user__username=username)
    base_url = profile.get_absolute_url()

    return render(request, template, {
        'history': json.dumps(history),
        'base_url': base_url,
    })
