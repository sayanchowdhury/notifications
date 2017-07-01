from django.forms import ModelForm

from gh.models import GHUser


class AddUserForm(ModelForm):
    class Meta:
        model = GHUser
        fields = ['username']
