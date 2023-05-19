from django.db import models
from django.contrib.auth.models import User

class Contatos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(blank=True)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    altura = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
    descricao = models.TextField()
    data_nascimento = models.DateField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Contatos'
    

