from django.urls import path
from . import views

urlpatterns = [
    path('/add_medico', views.lista_herois, name='lista_herois'),
    path('/add_especialidade', views.lista_herois, name='lista_herois'),
    path('listar_medico', views.listar_medico, name='listar_medico'),
    path('listar_especialidade', views.listar_especialidade, name='listar_especialidade'),
    
]