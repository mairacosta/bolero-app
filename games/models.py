from django.db import models

from groups.models import Group
from players.models import Player


class Game(models.Model):
    name = models.CharField(verbose_name='nome', max_length=63)
    date_time = models.DateTimeField(verbose_name='data e hora')
    players = models.ManyToManyField(Player, related_name='games', verbose_name='jogadores')
    group = models.ForeignKey(Group, verbose_name='grupo', on_delete=models.CASCADE)
    local = models.CharField(verbose_name='local da partida', max_length=255)
    max_players = models.IntegerField(verbose_name='quantidade máxima de jogadores')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'jogo'
        verbose_name_plural = 'jogos'
