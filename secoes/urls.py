from django.urls import path
from .views import (
    GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView,
    CommentCreateView, CategoryListView, CategoryDetailView
)
from . import views

app_name = 'secoes'

urlpatterns = [
    path('', GameListView.as_view(), name='index'),
    path('search/', views.search_games, name='search'),
    path('create/', GameCreateView.as_view(), name='create'),
    path('<int:pk>/', GameDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', GameUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', GameDeleteView.as_view(), name='delete'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]



