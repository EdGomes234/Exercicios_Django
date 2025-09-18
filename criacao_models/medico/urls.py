from django.urls import path
from . import views

urlpatterns = [
    path('add_especialidade/', views.CreateEspecialidade.as_view(), name='add_especialidade'),
    path('list_especialidade/', views.ListEspecialidade.as_view(), name='list_especialidade'),

    path('add_medico/', views.CreateMedico.as_view(), name='add_medico'),
    path('list_medico/', views.ListMedico.as_view(), name='list_medico'),
]