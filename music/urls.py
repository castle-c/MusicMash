from django.conf.urls import url
from . import views #from this folder import views file


urlpatterns = [
#/music/
    url(r'^$', views.index, name='index'),
    #when music page loads go to views and run this function

    #/music/99
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
