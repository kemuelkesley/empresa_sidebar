from django.contrib import admin
from empresa.models import Funcionario


# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'idade', 'salario', 'sexo', 'data_nascimento', 'cpf', 'email')



admin.site.register(Funcionario, FuncionarioAdmin)
