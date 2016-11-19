from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
  artist = models.CharField(max_length=250)
  album_title = models.CharField(max_length=250)
  genre = models.CharField(max_length=100)
  album_logo = models.CharField(max_length=1000)

  def get_absolute_url(self):
    return reverse('music:detail', kwargs={'pk': self.pk})
#first paramater passed in is view, takes primary key of album were trying to view details of
#second parameter is primary key of whichever object is created

  def __str__(self): #Album.objects.all() now returns a readable string
    return self.album_title + ' - ' + self.artist

class Song(models.Model):
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  file_type = models.CharField(max_length=10)
  song_title = models.CharField(max_length=250)
  is_favorite = models.BooleanField(default=False)

  def __str__(self):
    return self.song_title
