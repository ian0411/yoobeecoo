from django.conf.urls import url

from newsletters.views import control_newsletter, control_newsletter_list, control_newsletter_detail

urlpatterns = [
    url(r'^newsletter/$', control_newsletter, name='control_newsletter'),
    url(r'^newsletter-list/$', control_newsletter_list, name='control_newsletter_list'),
    url(r'^newsletter-detail/(?P<pk>\d+)/$', control_newsletter_detail, name='control_newsletter_detail'),
]
