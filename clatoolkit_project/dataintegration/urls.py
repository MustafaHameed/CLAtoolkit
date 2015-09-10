
from django.conf.urls import patterns, url

from dataintegration import views

urlpatterns = patterns(
    url(r'^home/$', views.home, name='home'),
    url(r'^login/(?P<group_id>\d+)$', views.login, name='login'),
    url(r'^get_social/$', views.get_social_media_id, name='get_social'),
    url(r'^refreshtwitter/$', views.refreshtwitter, name='refreshtwitter'),
    url(r'^refreshyoutube/$', views.refreshyoutube, name='refreshyoutube'),
	url(r'^ytAuthCallback/$', views.ytAuthCallback, name='ytAuthCallback'),
    #url(r'^refreshGoogleDrive/$', views_gd.refreshGoogleDrive, name='refreshGoogleDrive'),
    #url(r'^gdAuthCallback/$', views_gd.gdAuthCallback, name='gdAuthCallback'),
    #url(r'^gdindex/$', views_gd.gdindex),
)
