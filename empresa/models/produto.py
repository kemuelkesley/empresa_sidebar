from django.db import models

# Create your models here.

class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    descricao = models.TextField()
    quantidade = models.IntegerField(null=True)

    def __str__(self):
        return self.nome


