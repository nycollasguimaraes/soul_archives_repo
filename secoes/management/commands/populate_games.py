from django.core.management.base import BaseCommand
from secoes.models import Game
from secoes.temp_data import game_data

class Command(BaseCommand):
    help = "Popula o banco de dados com games do temp_data.py"

    def handle(self, *args, **kwargs):
        for g in game_data:
            Game.objects.create(
                name=g["name"],
                release_year=int(g["release_year"]),
                poster_url=g["poster_url"]
            )
        self.stdout.write(self.style.SUCCESS("Games inseridos com sucesso!"))
