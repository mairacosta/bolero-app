from django.db import models

from groups.models import Group
from players.models import Player


class Game(models.Model):
    date_time = models.DateTimeField(verbose_name='data e hora')
    players = models.ManyToManyField(Player, related_name='games', verbose_name='jogadores')
    group = models.ForeignKey(Group, verbose_name='grupo', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_time)
    
    class Meta:
        verbose_name = 'jogo'
        verbose_name_plural = 'jogos'
