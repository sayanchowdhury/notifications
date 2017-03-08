
from django.shortcuts import render
from django.template import RequestContext


def index(request):
    """
    This is the home of Notifications.
    """
    template = 'app/index.html'

    return render(request, template, {
        'message': 'Hello World'
    })
