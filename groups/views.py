from django.shortcuts import get_object_or_404, render

from django.contrib.auth.decorators import login_required
from games.models import Game
from groups.forms import GroupCreateForm
from players.services import get_player
from .services import create_group, delete_group, get_group, get_player_groups, player_has_permission, subscribe_player_in_group, unsubscribe_player_in_group
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import Group


@login_required
def index(request):
    code = request.GET.get('code')
    if code:
        group_found = Group.objects.filter(code=code).first()
    else:
        group_found = None
    groups = get_player_groups(request.user)
    return render(request, "groups/index.html", {
        'groups': groups, 'group_found': group_found
    })

@login_required
def create(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            group = create_group(form.cleaned_data, request.user)
            messages.success(request, f'Grupo {group} criado.')
            return redirect(reverse('groups'))
        else:
            messages.error(request, f'Dados inválidos: {form.errors}')
    else:
        form = GroupCreateForm()
        group = None
    return render(request, "groups/create.html", {
        'form': form, 'group': group
    })

@login_required
def edit(request, code):
    group = get_group(code)
    if not group:
        messages.error(request, 'Grupo não encontrado.')
        return redirect(reverse('groups'))
    elif group.admin.user != request.user:
        messages.error(request, 'Usuário não tem permissão.')
        return redirect(reverse('groups'))

    if request.method == 'POST':
        form = GroupCreateForm(data=request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, f'Grupo {group} atualizado.')
            return redirect(reverse('group-detail', args=[group.code]))
        else:
            messages.error(request, f'Dados inválidos: {form.errors}')
    else:
        form = GroupCreateForm(instance=group)
    return render(request, "groups/edit.html", {
        'form': form, 'group': group
    })

@login_required
def remove(request, code):
    group = get_group(code)
    if not group:
        messages.error(request, 'Grupo não encontrado.')
        return redirect(reverse('groups'))
    elif group.admin.user != request.user:
        messages.error(request, 'Usuário não tem permissão.')
        return redirect(reverse('groups'))

    delete_group(group)
    messages.success(request, f'Grupo {group} removido com sucesso!')
    return redirect(reverse('groups'))

@login_required
def detail(request, code):
    group = get_object_or_404(Group, code=code)
    player = get_player(request.user)
    player_in_group = player_has_permission(group, player)
    if player_in_group:
        games = Game.objects.filter(group=group)
    else:
        games = None

    return render(request, "groups/detail.html", {
        'group': group, 
        'games': games, 
        'player_in_group': player_in_group,
        'user_player': player
    })

@login_required
def subscribe(request, code):
    group = get_object_or_404(Group, code=code)
    player = get_player(request.user)
    
    if not player_has_permission(group, player):
        subscribe_player_in_group(group, player)
        messages.success(request, f'Jogagor {player} se inscreveu no grupo {group}')
    else:
        messages.warning(request, f'Jogador já inscrito neste grupo.')
            
    return redirect(reverse('group-detail', args=[code]))

@login_required
def unsubscribe(request, code):
    group = get_object_or_404(Group, code=code)
    player = get_player(request.user)
    
    if player_has_permission(group, player):
        unsubscribe_player_in_group(group, player)
        messages.warning(request, f'Jogagor {player} saiu do grupo {group}')
    else:
        messages.warning(request, f'Jogador não está inscrito neste grupo.')
            
    return redirect(reverse('group-detail', args=[code]))