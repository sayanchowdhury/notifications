from django.shortcuts import render


def dashboard(request, username):
    """
    Comment goes here
    """
    template = 'profiles/dashboard.html'
    return render(request, template, {
        'message': 'Hello World'
    })
