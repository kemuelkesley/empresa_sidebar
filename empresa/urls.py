from django.urls import path
from empresa.views import index, lista_funcionarios, cadastrar_funcionario, editar_funcionario
from empresa.views import listar_produtos


urlpatterns = [
   path('', index, name='index'),
   path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
   path('cadastrar_funcionario/', cadastrar_funcionario, name='cadastrar_funcionario'),
   path('editar_funcionario/<int:id>', editar_funcionario, name='editar_funcionario'),
   # Produtos
   path('produtos/', listar_produtos, name='listar_produtos'),
]
