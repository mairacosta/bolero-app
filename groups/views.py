from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from groups.forms import GroupCreateForm
from .services import create_group, get_player
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import Group


@login_required
def index(request):
    groups = Group.objects.filter(players=get_player(request.user))
    return render(request, "groups/index.html", {
        'groups': groups
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
        form = GroupCreateForm()
        group = None
    return render(request, "groups/create.html", {
        'form': form, 'group': group
    })

@login_required
def detail(request, code):
    group = Group.objects.get(code=code)
    return render(request, "groups/detail.html", {
        'group': group
    })
