from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Produto (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.nome
    
class CustomUser(AbstractUser):
    ADMIN = 'admin'
    OPERADOR = 'operador'
    TIPOS_USUARIO = [
        (ADMIN, 'Administrador'),
        (OPERADOR, 'Operador'),
    ]
    tipo_usuario = models.CharField(
        max_length=50, choices=TIPOS_USUARIO, default=OPERADOR
    )
    data_nascimento = models.DateField(null=True, blank=True)