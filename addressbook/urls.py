from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)

import contacts.views

urlpatterns = patterns('',
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^new$', contacts.views.CreateContactView.as_view(),
        name='contacts-new',),
    url(r'^query$', contacts.views.CreateQueryView.as_view(),
        name='contacts-query',),
    #url(r'^new$', contacts.views.QueryContactView.as_view(),
    #    name='contacts-query',),
)