from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.nome   