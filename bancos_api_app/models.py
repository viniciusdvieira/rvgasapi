from django.db import models

class Banco(models.Model):
    codigo_compensacao = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário

    def __str__(self):
        return self.nome