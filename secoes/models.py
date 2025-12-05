from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=200)
    release_year = models.IntegerField()
    poster_url = models.URLField()

    def __str__(self):
        return self.name