from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import *
from .forms import AddForm


# Create your views here.
class CreateEspecialidade(CreateView):
    model = Especialidade
    form_class = AddForm
    template_name = 'medico/add_especialidade.html'
    success_url = reverse_lazy('list_especialidade')

class CreateMedico(CreateView):
    model = Medico
    form_class = AddForm
    template_name = 'medico/add_medico.html'
    success_url = reverse_lazy('list_medico')

class ListMedico(ListView):
    model = Medico
    template_name = 'medico/list_medico.html'
    context_object_name = 'medicos'

class ListEspecialidade(ListView):
    model = Especialidade
    template_name = 'medico/list_especialidade.html'
    context_object_name = 'especialidades'
    
