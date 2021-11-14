from django.db import models

from players.models import Player


class Group(models.Model):
    name = models.CharField(verbose_name='nome', max_length=255)
    code = models.CharField(verbose_name='código', max_length=36)
    admin = models.ForeignKey(Player, verbose_name='administrador', on_delete=models.SET_NULL, null=True)
    players = models.ManyToManyField(Player, related_name='groups', verbose_name='jogadores')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'grupo de jogadores'
        verbose_name_plural = 'grupos de jogadores'
