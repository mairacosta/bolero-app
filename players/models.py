from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.ForeignKey(User, verbose_name='usuário', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)