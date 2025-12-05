from django.core.management.base import BaseCommand
from secoes.models import Game, Category, Comment
from django.contrib.auth.models import User
from django.utils import timezone

class Command(BaseCommand):
    help = "Popula o banco com todos os jogos, categorias e comentários de exemplo"

    def handle(self, *args, **kwargs):
        # 1. Criar categorias
        categories_data = [
            {"name": "RPG", "description": "Jogos de Role Playing Game"},
            {"name": "Action", "description": "Jogos de ação"},
            {"name": "Souls-like", "description": "Jogos do estilo Souls"},
            {"name": "Open World", "description": "Jogos de mundo aberto"},
        ]

        categories = []
        for c in categories_data:
            category, created = Category.objects.get_or_create(
                name=c["name"], defaults={"description": c["description"]}
            )
            categories.append(category)
        self.stdout.write(self.style.SUCCESS("Categorias inseridas com sucesso!"))

        # 2. Dados dos jogos
        games_data = [
            {"name": "Dark Souls", "release_year": 2011, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/570940/header.jpg"},
            {"name": "Dark Souls II", "release_year": 2014, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/236430/header.jpg"},
            {"name": "Dark Souls III", "release_year": 2016, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/374320/header.jpg"},
            {"name": "Sekiro: Shadows Die Twice", "release_year": 2019, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/814380/header.jpg"},
            {"name": "Elden Ring", "release_year": 2022, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1245620/header.jpg"},
            {"name": "Lies of P", "release_year": 2023, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1627720/header.jpg"},
            {"name": "Nioh", "release_year": 2017, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/485510/header.jpg"},
            {"name": "Nioh 2", "release_year": 2020, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1325200/header.jpg"},
            {"name": "Wo Long: Fallen Dynasty", "release_year": 2023, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1448440/header.jpg"},
            {"name": "Mortal Shell", "release_year": 2020, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1110910/header.jpg"},
            {"name": "Lords of the Fallen (2014)", "release_year": 2014, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/265300/header.jpg"},
            {"name": "Lords of the Fallen (2023)", "release_year": 2023, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1501750/header.jpg"},
            {"name": "Remnant: From the Ashes", "release_year": 2019, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/617290/header.jpg"},
            {"name": "Remnant II", "release_year": 2023, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1282100/header.jpg"},
            {"name": "Code Vein", "release_year": 2019, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/678960/header.jpg"},
            {"name": "Salt and Sanctuary", "release_year": 2016, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/283640/header.jpg"},
            {"name": "Salt and Sacrifice", "release_year": 2022, "poster_url": "https://static.gog-cdn.com/product_images/85a3beae43145e3f0400fffccf1439688772d61e95762d1cdad7a1a1e8ff80ba.jpg"},
            {"name": "Blasphemous", "release_year": 2019, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/774361/header.jpg"},
            {"name": "Blasphemous 2", "release_year": 2023, "poster_url": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2114740/header.jpg"},
        ]

        # 3. Criar superusuário para comentários
        user, created = User.objects.get_or_create(username="admin")
        if created:
            user.set_password("admin123")
            user.is_superuser = True
            user.is_staff = True
            user.save()
        self.stdout.write(self.style.SUCCESS("Usuário admin criado!"))

        # 4. Criar jogos, associar categorias e comentários
        for i, g in enumerate(games_data):
            game, created = Game.objects.get_or_create(
                name=g["name"],
                defaults={"release_year": g["release_year"], "poster_url": g["poster_url"]}
            )
            # Associar 2 categorias a cada jogo
            game.categories.add(categories[i % len(categories)])
            game.categories.add(categories[(i+1) % len(categories)])

            # Criar 2 comentários por jogo
            Comment.objects.create(post=game, author=user, text="Jogo incrível!", created_at=timezone.now())
            Comment.objects.create(post=game, author=user, text="Difícil, mas recompensador.", created_at=timezone.now())

        self.stdout.write(self.style.SUCCESS("Todos os jogos receberam categorias e comentários!"))
