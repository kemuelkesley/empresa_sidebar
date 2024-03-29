from django import forms
from empresa.models.funcionario import Funcionario, Cargo, Genero
from empresa.models.produto import Produto, Categoria

class FuncionarioForm(forms.ModelForm):


    nome = forms.CharField(        
        label='Nome', 
        max_length=50,
        required=True,   
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Digite seu nome',
        }),          
    )

    cargo = forms.ModelChoiceField(
        label='Cargo',
        queryset=Cargo.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )
   

    salario = forms.DecimalField(
        label='Salário',
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'R$ 0,00',
        }),
    )

    

    genero = forms.ModelChoiceField(
        label='Genero',
        queryset=Genero.objects.all(),          
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )

   
    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': '00/00/0000',
        }),        
    )

    cpf = forms.CharField(        
        label='CPF', 
        max_length=11,
        required=True,   
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Informe o CPF',
        }),          
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Informe o e-mail',
        }),
    ) 

    telefone = forms.CharField(
        label='Telefone',
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(00) 0 0000-0000',
        }),
    )

    data_admissao = forms.DateField(
        label='Data de Admissão',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': '00/00/0000',
        }),
    )


    data_demissao = forms.DateField(
        label='Data de Demissão',
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': '00/00/0000',
        }),
    )



    cep = forms.CharField(
        label='CEP',
        max_length=8,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '00000-000',
        }),
    )

    logradouro = forms.CharField(
        label='Logradouro',
        max_length=40,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Informe o logradouro',
        }),
    )

    numero = forms.CharField(
        label='Número',
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Informe o número',
        }),
    )    

    bairro = forms.CharField(
        label='Bairro',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Informe o bairro',
        }),
    )

    localidade = forms.CharField(
        label='Localidade',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Informe a localidade',
        }),
    )

    uf = forms.CharField(
        label='UF',
        max_length=2,
        required=False,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Informe a UF',
        })
    )


    class Meta:
        model = Funcionario
        fields = '__all__'



class ProdutoForm(forms.ModelForm):

    nome = forms.CharField(
        label='Nome',
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome do produto',
        }),
    )


    categoria = forms.ModelChoiceField(
        label='Categoria',
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )

    preco = forms.DecimalField(
        label='Preço',
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'R$ 0,00',            
        }),
    )

    descricao = forms.CharField(
        label='Descrição',
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'cols': 20,
            'class': 'form-control',
            'placeholder': 'Informe a descrição do produto',
        }),
    )

    quantidade = forms.IntegerField(
        label='Quantidade',
        required=False,        
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Informe a quantidade',
        }),
    )

    class Meta:
        model = Produto
        fields = '__all__'
        exclude = ['codigo']



class CategoriaForm(forms.ModelForm):

    nome = forms.CharField(
        label='Categoria',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome da Categoria',
        }),
    )

    class Meta:
        model = Categoria
        fields = '__all__'
        exclude = ['codigo']