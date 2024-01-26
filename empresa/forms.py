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
            'placeholder': 'Informe o Salário',
        }),          
    ) 

    class Meta:
        model = Funcionario
        fields = ('nome', 'cargo', 'idade', 'salario')
