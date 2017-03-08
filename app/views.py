from django.shortcuts import render_to_response

# Create your views here.


def index(request):
    """
    This is the home of Notifications.
    """
    ctx = {
        'message': 'Hello World'
    }
    return render_to_response('app/index.html', ctx)
