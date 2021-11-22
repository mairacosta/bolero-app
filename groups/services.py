from players.models import Player
from .models import Group
from uuid import uuid4


def create_group(cleaned_data, user):
    player = get_player(user)
    group = Group(
        name=cleaned_data['name'],
        code=create_code(),
        admin=player,
    )
    group.save()
    group.players.add(player)
    return group

def create_code():
    return str(uuid4())

def get_player(user):
    player, created = Player.objects.get_or_create(user=user)
    return player