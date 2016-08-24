from django.conf.urls import url
from . import views #from this folder import views file
app_name = 'music'
#gives details,index html access to url by using 'music':'favorite' syntax

urlpatterns = [
#/music/
    url(r'^$', views.index, name='index'),
    #when music page loads go to views and run this function

    #/music/<albumid>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #/music/<albumid>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    #finds id of the song thatis selected and passes it to favorite url
    # and sets is_favorite to true than redirects user to same page

]
