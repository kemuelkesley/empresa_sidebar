from django.shortcuts import redirect, render
from empresa.models import Funcionario
from empresa.forms import FuncionarioForm

from django.contrib import messages

# Create your views here.

def index(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'index.html', {'funcionarios' : funcionarios})



def cadastrar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()           
            messages.success(request, 'Funcionário cadastrado com sucesso.')
            # return render(request, 'index.html')
            return redirect('index')
        else:
          messages.error(request, 'Erro ao cadastrar funcionário. Verifique os campos.')
    
    else:
        form = FuncionarioForm()

    return render(request, 'cadastrar_funcionario.html', {'form': form})


def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'lista_funcionarios.html', {'funcionarios': funcionarios})