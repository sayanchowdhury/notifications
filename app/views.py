from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse


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


@login_required
def logout_view(request):
    """
    This view logs the user out of the current session.
    """
    if request.user.is_authenticated():
        logout(request)
        return redirect(reverse('app_index'))
