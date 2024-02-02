from django.contrib import admin
from empresa.models.funcionario import Funcionario, Cargo, Genero
from empresa.models.produto import Categoria, Produto


# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'salario', 'genero', 'data_nascimento', 'cpf', 'email')



admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo)
admin.site.register(Genero)


# produtos

admin.site.register(Categoria)
admin.site.register(Produto)
