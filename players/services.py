from .models import Player


def get_player(user):
    player, created = Player.objects.get_or_create(user=user)
    return player