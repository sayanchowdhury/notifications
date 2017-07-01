from django.shortcuts import render

from .forms import AddUserForm
from .models import GHIssues

def add_user(request):
    template = 'add_user.html'

    form = AddUserForm()

    ctx = {
        'form': form,
    }

    return render(request, template, context=ctx)


def show_all_issues(request):
    template = 'list_issues.html'

    user = request.user
    issues = GHIssues.objects.filter(user=user)

    ctx = {
        'issues': issues
    }

    return render(request, template, context=ctx)
