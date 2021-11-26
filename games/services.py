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

def get_game(group, id):
    return Game.objects.filter(group=group, id=id).first()

def delete_game(game):
    Game.objects.filter(id=game.id).delete()