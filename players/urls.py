from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_player, name='player-create'),
    path('edit', views.edit, name='player-edit'),
    path('remove', views.remove, name='player-remove'),
]
