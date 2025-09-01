from django.db import models

#EDGAR GOMES OLIVEIRA

# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=20)
    id_especialidade = models.ForeignKey('Especialidade', on_delete=models.CASCADE)


class Especialidade(models.Model):
    nome = models.CharField()
    descricao = models.TextField()