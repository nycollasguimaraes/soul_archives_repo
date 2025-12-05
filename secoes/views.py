from .temp_data import game_data
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Game

class GameListView(ListView):
    model = Game
    template_name = "secoes/index.html"
    context_object_name = "game_list"

class GameDetailView(DetailView):
    model = Game
    template_name = "secoes/detail.html"

class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'release_year', 'poster_url']
    template_name = "secoes/create.html"
    success_url = reverse_lazy('secoes:index')

class GameUpdateView(UpdateView):
    model = Game
    fields = ['name', 'release_year', 'poster_url']
    template_name = "secoes/update.html"
    success_url = reverse_lazy('secoes:index')

class GameDeleteView(DeleteView):
    model = Game
    template_name = "secoes/delete.html"
    success_url = reverse_lazy('secoes:index')

def search_games(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "game_list": [
                g for g in game_data
                if request.GET['query'].lower() in g['name'].lower()
            ]
        }
    return render(request, 'secoes/search.html', context)
