from games.models import Game
from players.services import get_player


def create_game(cleaned_data, user, group):
    game = Game(group=group, **cleaned_data)
    game.save()
    game.players.add(get_player(user))
    return game

def subscribe_player(game, player):
    game.players.add(player)

def unsubscribe_player(game, player):
    game.players.remove(player)