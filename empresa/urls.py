from django.urls import path
from empresa.views import index, lista_funcionarios, cadastrar_funcionario, editar_funcionario
from empresa.views import listar_categoria, listar_produtos, filtrar_produtos




urlpatterns = [
   path('', index, name='index'),
   path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
   path('cadastrar_funcionario/', cadastrar_funcionario, name='cadastrar_funcionario'),
   path('editar_funcionario/<int:id>', editar_funcionario, name='editar_funcionario'),
   # Produtos
   path('categoria/', listar_categoria, name='listar_categoria'),
   path('produtos/', listar_produtos, name='listar_produtos'),
   path('filtrar_produtos/<int:id>/', filtrar_produtos, name='filtrar_produtos'),
   #path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
]
