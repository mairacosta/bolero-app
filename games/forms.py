from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Game


class GameCreateForm(ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'date_time', 'local', 'max_players']