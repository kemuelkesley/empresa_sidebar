from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome




class Funcionario(models.Model):

    SEXO_CHOICES = (
        ('E', '---------'),
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )

    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)   
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=11, null=True, blank=True)
    

    def __str__(self):
        return self.nome   