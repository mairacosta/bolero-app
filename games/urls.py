from django.urls import path
from . import views

urlpatterns = [
    path('<code>/game-create/', views.create, name='game-create'),
    path('<code>/game-remove/<game_id>', views.remove, name='game-remove'),
    path('<code>/game-edit/<game_id>', views.edit, name='game-edit'),
    path('<code>/game-subscribe/<game_id>', views.subscribe, name='game-subscribe'),
    path('<code>/game-unsubscribe/<game_id>', views.unsubscribe, name='game-unsubscribe'),
]
