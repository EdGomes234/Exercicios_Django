from django.urls import path
from . import views

urlpatterns = [
    path('add_medico', views.add_medico, name='add_medico'),
    path('add_especialidade', views.add_especialidade, name='add_especialidade'),
    path('listar_medico', views.listar_medico, name='listar_medico'),
    path('listar_especialidade', views.listar_especialidade, name='listar_especialidade'),
    
]