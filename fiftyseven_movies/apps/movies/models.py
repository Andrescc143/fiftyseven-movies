from django.db import models
from apps.users.models import User


class Gener(models.Model):
    name = models.CharField("Gener name", max_length=80)
    
    class Meta:
        verbose_name = "Gener"
        verbose_name_plural = "Geners"

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField("Language name", max_length=80)
    
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField("Title", max_length=150, unique=True, null=False)
    release_date = models.DateField("Release_Date", null=False)
    rating = models.FloatField("Rating", null=False)
    gener = models.ForeignKey(Gener, verbose_name="Gener", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name="Language", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
    

class MoviePlaylist(models.Model):
    title = models.CharField("Title", max_length=150, unique=True, null=False)
    created_date = models.TimeField("Created", auto_now=False, auto_now_add=True)
    public= models.BooleanField(default = True)
    rating = models.FloatField("Rating", null=False)
    movies = models.ManyToManyField(Movie, related_name='playlists')
    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = "MoviePlaylist"
        verbose_name_plural = "MoviePlaylists"

    def __str__(self):
        return self.title
    