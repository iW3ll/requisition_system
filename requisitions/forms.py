from django import forms
from .models.models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome_estudante', 'matricula', 'email', 'curso', 'bolsista_pae', 'deseja_caderno', 'deseja_garrafa', 'camisa']
        
