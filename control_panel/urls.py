from django.conf.urls import url

from newsletters.views import control_newsletter

urlpatterns = [
    url(r'^newsletter/$', control_newsletter, name='control_newsletter'),
]
