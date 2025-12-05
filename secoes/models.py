from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()
    poster_url = models.URLField()
    categories = models.ManyToManyField(Category, related_name='games', blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']  # mais recente primeiro

    def __str__(self):
        return f'{self.author.username} - {self.text[:20]}'
