from django.shortcuts import redirect, render
from empresa.models.funcionario import Funcionario
from empresa.forms import FuncionarioForm, ProdutoForm, CategoriaForm

from django.contrib import messages

from empresa.models.produto import Produto, Categoria

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
          print(form.errors.as_data())
    
    else:
        form = FuncionarioForm()

    return render(request, 'funcionario/cadastrar_funcionario.html', {'form': form})


def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/lista_funcionarios.html', {'funcionarios': funcionarios})


def editar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        messages.success(request, 'Funcionário atualizado com sucesso.')
        return redirect('lista_funcionarios')
    else:
        messages.error(request, 'Erro ao atualizar funcionário. Verifique os campos.')

    return render(request, 'funcionario/editar_funcionario.html', {'form': form, 'funcionario': funcionario})


# Produtos


def listar_categoria(request):
    
    form_categoria = CategoriaForm()

    if request.method == 'POST':
        form_categoria = CategoriaForm(request.POST)
        if form_categoria.is_valid():
            form_categoria.save()
            # Talvez adicione uma mensagem de sucesso aqui, se desejar
            return redirect('listar_categoria')  # Redirecionar após o POST

    categorias = Categoria.objects.all()
    return render(request, 'produto/categorias.html', {'form_categoria': form_categoria, 'categorias': categorias})

def listar_produtos(request):
    produtos = Produto.objects.all()
    form_produto = ProdutoForm()

    if request.method == 'POST':
        form_produto = ProdutoForm(request.POST)
        if form_produto.is_valid():
            form_produto.save()
            messages.success(request, 'Produto cadastrado com sucesso.')
            return redirect('listar_produtos')
        else:
            messages.error(request, 'Erro ao cadastrar produto. Verifique os campos.')
            print(form_produto.errors.as_data())

    return render(request, 'produto/listar_produtos.html', {'produtos': produtos, 'form_produto': form_produto})


def filtrar_produtos(request, id):
    categoria = Categoria.objects.get(codigo=id)
    print(f'Categoria: {categoria.nome}')
    produtos = Produto.objects.filter(categoria=categoria)
    quantidade_produtos = produtos.count()
    print(f'Produtos: {produtos}')
    return render(request, 'produto/produtos_por_categoria.html', {'categoria': categoria, 'produtos': produtos, 'quantidade_produtos': quantidade_produtos})


# def cadastrar_produto(request):
#     form_produto = ProdutoForm()

#     return render(request, 'produto/listar_produtos.html', {'form_produto': form_produto})

   