from django.contrib import admin
from .models import Game, Comment, Category

admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Category)