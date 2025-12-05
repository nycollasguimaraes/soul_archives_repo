from .temp_data import game_data
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Comment, Game
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404


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

class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']
    template_name = 'secoes/create_comment.html'

    def form_valid(self, form):
        # Aqui pegamos o game pelo pk da URL
        game = get_object_or_404(Game, pk=self.kwargs['pk'])
        form.instance.post = game        # atribui o post
        form.instance.author = self.request.user  # atribui o autor logado
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('secoes:detail', kwargs={'pk': self.kwargs['pk']})
