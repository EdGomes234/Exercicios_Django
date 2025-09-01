from django.contrib import admin
from .models import Medico, Especialidade
# Register your models here.

# EDGAR GOMES OLIVEIRA


class MedicoAdmin(admin.ModelAdmin):
    fields = [
        "nome",
        "endereco",
        "telefone",
        "email",
        "data_nascimento",
        "crm",
        "id_especialidade"
    ]

class EspecialidadeAdmin(admin.ModelAdmin):
    fields = [
        "nome",
        "descricao"
    ]

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)