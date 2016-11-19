from django.conf.urls import url
from . import views #from this folder import views file
app_name = 'music'
#gives details,index html access to url by using 'music':'favorite' syntax

urlpatterns = [
#/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #when music page loads go to views and run this function

    # url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),


    #/music/<albumid>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #music/album/2/
    url(r'album/add$', views.AlbumCreate.as_view(), name='album-add'),

    #music/album/2/update
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='album-delete'),
]
