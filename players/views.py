from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages

from django.contrib.auth import views
from django.urls.base import reverse

from players.forms import PlayerCreateForm


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
