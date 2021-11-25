from players.models import Player
from .models import Group
from uuid import uuid4
from players.services import get_player


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

def get_player_groups(user):
    return Group.objects.filter(players=get_player(user))

def player_has_permission(group, player):
    return group.players.filter(
        user_id=player.user
    ).exists()

def subscribe_player_in_group(group, player):
    group.players.add(player)

def unsubscribe_player_in_group(group, player):
    group.players.remove(player)