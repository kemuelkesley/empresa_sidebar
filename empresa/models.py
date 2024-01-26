from django.db import models

# Create your models here.

class Funcionario(models.Model):

    SEXO_CHOICES = (
        ('E', 'Escolha...'),
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    

    def __str__(self):
        return self.nome   