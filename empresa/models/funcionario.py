from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome



class Funcionario(models.Model):
    
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)   
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=11, null=True, blank=True)
    data_admissao = models.DateField(null=True, blank=True)
    data_demissao = models.DateField(null=True, blank=True)

    #Endereço
    cep = models.CharField(max_length=8, null=True, blank=True)
    logradouro = models.CharField(max_length=50, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    localidade = models.CharField(max_length=50, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)


    def __str__(self):
        return self.nome   