from django.contrib.auth.models import User
from .models import Player


def get_player(user):
    player, _ = Player.objects.get_or_create(user=user)
    return player
