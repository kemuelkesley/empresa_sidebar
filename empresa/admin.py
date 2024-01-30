from django.contrib import admin
from empresa.models import Funcionario, Cargo


# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'salario', 'sexo', 'data_nascimento', 'cpf', 'email')



admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo)
