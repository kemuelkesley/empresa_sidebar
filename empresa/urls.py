from django.urls import path
from empresa.views import index, lista_funcionarios, cadastrar_funcionario


urlpatterns = [
   path('', index, name='index'),
   path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
   path('cadastrar_funcionario/', cadastrar_funcionario, name='cadastrar_funcionario'),
]
