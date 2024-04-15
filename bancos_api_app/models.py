from django.db import models

class Instituicao(models.Model):
    codigo_compensacao = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
