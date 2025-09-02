from django.shortcuts import render
from .models import *
from .forms import AddForm


# Create your views here.
def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/list_medico.html', {"medicos": medicos})

def listar_especialidade(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'medico/list_especialidade.html', {"especialidades" : especialidades})

def add_especialidade(request):

        if request.method == 'POST':
        
            especialidade = AddForm(request.POST)

            if especialidade.is_valid():

                new_member_name = especialidade.data.get("nome")
                new_member_relation = especialidade.data.get("descricao")
                

                Especialidade.objects.create(
                    nome =  new_member_name, 
                    descricao = new_member_relation,
                    
                    )
                    
                especialidades = Especialidade.objects.all()
                return render(request, 'medico/list_especialidade.html', {"especialidades" : especialidades})   
            
            else:
                return render(request, 'medico/add_especialidade.html')
        else:
            return render(request, 'medico/add_especialidade.html')

def add_medico(request):


        if request.method == 'POST':
        
            medico = AddForm(request.POST)

            if medico.is_valid():

                new_member_name = medico.data.get("nome")
                new_member_endereco = medico.data.get("endereco")
                new_member_telefone = medico.data.get("telefone")
                new_member_email = medico.data.get("email")
                new_member_data_nascimento = medico.data.get("data_nascimento")
                new_member_crm = medico.data.get("crm")
                new_member_id_especialidade = medico.data.get("id_especialidade")
                especialidade = Especialidade.objects.get(id=new_member_id_especialidade)
                

                Medico.objects.create(
                    nome =  new_member_name, 
                    endereco = new_member_endereco,
                    telefone = new_member_telefone,
                    email = new_member_email,
                    data_nascimento = new_member_data_nascimento,
                    crm = new_member_crm,
                    id_especialidade = especialidade

                    )
                    
                medicos = Medico.objects.all()
                return render(request, 'medico/list_medico.html', {"medicos" : medicos})

            else:
                return render(request, 'medico/add_medico.html')
        else:
            especialidades = Especialidade.objects.all()
            return render(request, 'medico/add_medico.html', {"especialidades": especialidades})
