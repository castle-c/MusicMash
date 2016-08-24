from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
  all_albums = Album.objects.all()
  indexContext = {'all_albums': all_albums}
  return render(request, 'music/index.html', indexContext)

def detail(request, album_id):
  # album = Album.objects.get(pk=album_id)
  album = get_object_or_404(Album, pk=album_id)
  detailContext = {'album' : album}
  return render(request, 'music/details.html', detailContext)

def favorite(request, album_id):
  album = get_object_or_404(Album, pk=album_id)
  try:
    selected_song = album.song_set.get(pk=request.POST['song'])
    # get value of whatever song is selected ^
  except (KeyError, Song.DoesNotExist):
    #http request for details html file
    return render(request,'music/details.html', {
      'album' : album,
      'error_message': "please select a valid song",
      })

  else:
    selected_song.is_favorite = True
    selected_song.save()
    return render(request, 'music/details.html', {'album' : album})
