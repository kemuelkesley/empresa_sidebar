from django.contrib import admin
from empresa.models import Funcionario, Cargo, Genero


# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'salario', 'genero', 'data_nascimento', 'cpf', 'email')



admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo)
admin.site.register(Genero)
