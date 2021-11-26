from django.contrib.auth.forms import UserCreationForm

from players.services import get_player
from .models import Player


class PlayerCreateForm(UserCreationForm):
   
    def save(self):
        user = super().save()
        player = get_player(user)
        return player
        
