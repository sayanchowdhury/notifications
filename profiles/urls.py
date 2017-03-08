from __future__ import absolute_import

from django.conf.urls import url, include
from django.conf import settings

import profiles.views

urlpatterns = [
    url(r'^$',
        profiles.views.dashboard,
        name='profiles_dashboard')
]
