from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages

from django.contrib.auth import views
from django.urls.base import reverse

from players.forms import PlayerCreateForm, PlayerForm
from players.models import Player
from players.services import delete_player, get_player, update_player


class LoginView(views.LoginView):
    template_name = 'players/login.html'


def create_player(request):
    if request.method == 'POST':
        form = PlayerCreateForm(request.POST)
        if form.is_valid():
            player = form.save()
            messages.success(request, f'Usuário {player} criado com sucesso!')
            return redirect(reverse('login'))
        else:
            messages.error(request, f'Dados inválidos: {form.errors}')
    else:
        form = PlayerCreateForm()
    return render(request, "players/create.html", {
        'form': form
    })

@login_required
def edit(request):
    player = get_player(request.user)

    if request.method == 'POST':
        form = PlayerForm(data=request.POST, instance=player.user)
        if form.is_valid():
            update_player(player, form.cleaned_data)
            messages.success(request, f'Jogador {player} atualizado.')
            return redirect(reverse('groups'))
        else:
            messages.error(request, f'Dados inválidos: {form.errors}')
    else:
        form = PlayerForm(instance=player.user)
    return render(request, "players/edit.html", {
        'form': form, 'player': player
    })

@login_required
def remove(request):
    player = get_player(request.user)   
    delete_player(player)
    messages.success(request, f'Jogador {player} removido com sucesso!')
    return redirect(reverse('groups'))