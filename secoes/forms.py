from django import forms

class GameForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200)
    release_year = forms.IntegerField(label="Ano de Lançamento")
    poster_url = forms.URLField(label="URL do Poster")