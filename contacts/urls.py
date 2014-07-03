# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
#from django.conf.urls.defaults import *
from views import *

contact_patterns= patterns(
    '',
    url(r'^list/page(?P<page>[0-9]+)/(\?.*)?$',
        ContactListView.as_view(),
        name='list'),
    url(r'^update/(?P<pk>\d+)/$',
        ContactUpdateView.as_view(),
        name='update'),
    url(r'^create/$',
        ContactCreateView.as_view(),
        name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        ContactDeleteView.as_view(),
        name='delete'))


newpatterns = patterns(
    '',
    url(r'^contact/', include(contact_patterns, 
        namespace="contact")))


try:
    urlpatterns += newpatterns
except NameError:
    urlpatterns = newpatterns
