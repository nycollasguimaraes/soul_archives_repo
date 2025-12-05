from django.http import HttpResponse
from .temp_data import game_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def detail_game(request, game_id):
    context = {'game': game_data[game_id - 1]}
    return render(request, 'secoes/detail.html', context)

def list_games(request):
    context = {"game_list": game_data}
    return render(request, 'secoes/index.html', context)

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

def create_game(request):
    if request.method == 'POST':
        game_data.append({
            'id': str(len(game_data) + 1),
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('secoes:detail', args=(len(game_data),))
        )
    else:
        return render(request, 'secoes/create.html', {})
