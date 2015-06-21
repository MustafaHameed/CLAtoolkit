# example/example/urls.py

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social_data_integration.views.home', name='home'),
    # url(r'^social_data_integration/', include('social_data_integration.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fb_data/', include('fb_data.urls')),
                       url(r'^tw_data/', include('tw_data.urls')),
)
