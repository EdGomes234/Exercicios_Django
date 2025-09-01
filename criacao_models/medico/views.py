from django.shortcuts import render
from .models import *


# Create your views here.
def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/list_medico.html', {"medicos": medicos})

def listar_especialidade(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'medico/list_especialidade.html', {"especialidades" : especialidades})
