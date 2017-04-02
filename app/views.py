from django.shortcuts import render, redirect, reverse
from django.template import RequestContext


def index(request):
    """
    This is the home of Notifications.
    """
    if request.user.is_authenticated():
        username = request.user.username
        return redirect(reverse('profiles_dashboard', args=[username]))

    template = 'app/index.html'

    return render(request, template, {
        'message': 'Hello World'
    })
