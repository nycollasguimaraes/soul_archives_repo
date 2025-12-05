from django.urls import path
from . import views

app_name = 'secoes'

urlpatterns = [
    path('', views.list_games, name='index'),
    path('search/', views.search_games, name='search'),
    path('create/', views.create_game, name='create'),
    path('<int:game_id>/', views.detail_game, name='detail'),
    path('<int:game_id>/update/', views.update_game, name='update'),
    path('<int:game_id>/delete/', views.delete_game, name='delete'),
]
