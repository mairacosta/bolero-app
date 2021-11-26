from django.contrib.auth.models import User
from .models import Player


def get_player(user):
    player, _ = Player.objects.get_or_create(user=user)
    return player

def update_player(player, cleaned_data):
    player.user.username = cleaned_data['username']
    player.user.set_password(cleaned_data['password1'])
    player.user.save()

def delete_player(player):
    player.user.delete()
