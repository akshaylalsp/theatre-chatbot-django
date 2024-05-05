from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    image = models.CharField(max_length=50)
    inLanguage = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    datePublished = models.CharField(max_length=50)
    movie_detail_link = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    casts = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)

class Theatre(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)