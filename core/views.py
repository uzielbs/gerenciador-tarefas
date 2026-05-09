from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Tarefa
from .forms import TarefaForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def inicio(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('inicio')
    else:
        form = TarefaForm()

    tarefas = Tarefa.objects.filter(usuario=request.user).order_by('-criada_em')
    contexto = {
        'tarefas': tarefas,
        'form': form,
    }
    return render(request, 'core/inicio.html', contexto)

@login_required
def concluir(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.concluida = not tarefa.concluida
    tarefa.save()
    return redirect('inicio')

@login_required
def deletar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.delete()
    return redirect('inicio')
