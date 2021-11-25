from django.urls import path
from . import views

urlpatterns = [
    path('<code>/game-create/', views.create, name='game-create'),
    path('<code>/game-subscribe/<game_id>', views.subscribe, name='game-subscribe'),
    path('<code>/game-unsubscribe/<game_id>', views.unsubscribe, name='game-unsubscribe'),
]
