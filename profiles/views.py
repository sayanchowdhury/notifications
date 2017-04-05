import json

from django.shortcuts import render


def dashboard(request, username, param1=None):
    """
    Comment goes here
    """
    template = 'profiles/dashboard.html'
    base_url = 'http://localhost:8000/@sayanchowdhury/'
    history = []

    if param1 is None:
        param1 = 'dashboard'

    history.append(param1)

    return render(request, template, {
        'history': json.dumps(history),
        'base_url': base_url,
    })
