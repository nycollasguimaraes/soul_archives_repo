from django.core.management.base import BaseCommand
from secoes.models import Game, Category, Comment
from django.contrib.auth.models import User
from django.utils import timezone

class Command(BaseCommand):
    help = "Popula o banco com categorias e comentários de exemplo"

    def handle(self, *args, **kwargs):
        # Cria categorias
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

        # Associa categorias aos jogos
        games = Game.objects.all()
        for i, game in enumerate(games):
            # Distribuindo categorias de forma aleatória / sequencial
            game.categories.add(categories[i % len(categories)])

        self.stdout.write(self.style.SUCCESS("Categorias associadas aos jogos com sucesso!"))

        # Cria um superusuário para os comentários
        user, created = User.objects.get_or_create(username="admin")
        if created:
            user.set_password("admin123")  # defina uma senha
            user.is_superuser = True
            user.is_staff = True
            user.save()

        self.stdout.write(self.style.SUCCESS("Usuário admin criado!"))

        # Cria comentários de exemplo
        sample_comments = [
            "Jogo incrível!",
            "Difícil, mas recompensador.",
            "Gráficos espetaculares.",
            "Trilha sonora fantástica.",
        ]

        for game in games:
            for comment_text in sample_comments[:2]:  # 2 comentários por jogo
                Comment.objects.create(
                    post=game,
                    author=user,
                    text=comment_text,
                    created_at=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS("Comentários inseridos com sucesso!"))
