from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(blank = True, null = True, max_length = 500)
    author = models.CharField(blank = True, null = True, max_length = 500)
    lyrics = models.TextField(blank = True, null = True)
    image = models.ImageField(blank = True, null = True)