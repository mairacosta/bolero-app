from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls.base import reverse
from games.models import Game
from games.services import create_game, delete_game, get_game, subscribe_player, unsubscribe_player

from groups.models import Group
from groups.services import player_has_permission
from players.services import get_player
from .forms import GameCreateForm
from django.shortcuts import get_object_or_404
from django.contrib import messages


@login_required
def create(request, code):
    group = get_object_or_404(Group, code=code)
    if request.method == 'POST':
        form = GameCreateForm(request.POST)
        if form.is_valid():
            game = create_game(form.cleaned_data, request.user, group)
            messages.success(request, f'Jogo {game} criado com sucesso!')
            return redirect(reverse('group-detail', args=[group.code]))
        else:
            messages.error(request, f'Dados inválidos: {form.errors}')
    else:
        form = GameCreateForm()
    return render(request, "games/create.html", {
        'form': form
    })

@login_required
def edit(request, code, game_id):
    group = get_object_or_404(Group, code=code)
    game = get_game(group, game_id)
    if not group:
        messages.error(request, 'Jogo não encontrado.')
        return redirect(reverse('groups'))
    elif group.admin.user != request.user:
        messages.error(request, 'Usuário não tem permissão.')
        return redirect(reverse('groups'))

    if request.method == 'POST':
        form = GameCreateForm(data=request.POST, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, f'Jogo {game} atualizado.')
            return redirect(reverse('group-detail', args=[group.code]))
        else:
            messages.error(request, f'Dados inválidos: {form.errors}')
    else:
        form = GameCreateForm(instance=game)
    return render(request, "games/edit.html", {
        'form': form, 'game': game
    })

@login_required
def remove(request, code, game_id):
    group = get_object_or_404(Group, code=code)
    game = get_game(group, game_id)
    if not game:
        messages.error(request, 'Jogo não encontrado.')
        return redirect(reverse('group-detail', args=[code]))
    elif group.admin.user != request.user:
        messages.error(request, 'Usuário não tem permissão.')
        return redirect(reverse('group-detail', args=[code]))

    delete_game(game)
    messages.success(request, f'Jogo {game} removido com sucesso!')
    return redirect(reverse('group-detail', args=[code]))

@login_required
def subscribe(request, code, game_id):
    group = get_object_or_404(Group, code=code)
    game = get_object_or_404(Game, group=group, id=game_id)
    player = get_player(request.user)
    
    if player_has_permission(group, player):
        subscribe_player(game, player)
        messages.success(request, f'Jogagor {player} se inscreveu no jogo {game}')
    else:
        messages.warning(request, f'É necessário fazer parte do grupo para entrar neste jogo!')
            
    return redirect(reverse('group-detail', args=[code]))

@login_required
def unsubscribe(request, code, game_id):
    group = get_object_or_404(Group, code=code)
    game = get_object_or_404(Game, group=group, id=game_id)
    player = get_player(request.user)
    
    if player_has_permission(group, player):
        unsubscribe_player(game, player)
        messages.warning(request, f'Jogagor {player} saiu do jogo {game}')
    else:
        messages.error(request, f'É necessário fazer parte do grupo para sair deste jogo?!')
            
    return redirect(reverse('group-detail', args=[code]))