from django import forms
from empresa.models import Funcionario


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

    cargo = forms.CharField(        
        label='Cargo', 
        max_length=50,
        required=True,   
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Cargo do funcionário',
        }),          
    )  

    idade = forms.CharField(        
        label='Idade', 
        max_length=10,
        required=True,   
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Informe a idade',
        }),          
    ) 

    salario = forms.CharField(        
        label='Salario', 
        max_length=10,
        required=True,   
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'R$ 0,00',
        }),          
    )


    sexo = forms.ChoiceField(
        label='Sexo',
        choices=Funcionario.SEXO_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )

    data_nascimento = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={
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
            'placeholder': '(00) 0 0000-0000)',
        }),
    )

    class Meta:
        model = Funcionario
        fields = '__all__'