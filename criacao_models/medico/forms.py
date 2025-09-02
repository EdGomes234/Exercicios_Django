from django import forms
from .models import *

class AddForm(forms.Form):

    class Meta:
        model = Medico
        fields = ('nome', 'endereco', 'telefone','email', 'data_nascimento','crm','id_especialidade')

    class Meta:
        model = Especialidade
        fields = ('nome','descricao')