from django.shortcuts import render, redirect  # Adicionando redirect
from ..forms import EstudanteForm  # Importação corrigida
from ..models.models import Requisicao

def listar_requisicoes(request):
    requisicoes = Requisicao.objects.all()
    return render(request, 'requisitions/listar_requisicoes.html', {'requisicoes': requisicoes})

def home(request):
    return render(request, 'requisitions/home.html')

def cadastrar_estudante(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Certifique-se de que 'home' existe no urls.py
    else:
        form = EstudanteForm()
    return render(request, 'requisitions/cadastrar_estudante.html', {'form': form})
