from django.db import models


class Empresa(models.Model):
    nome = models.CharField(Max_length=100, help_text='Nome da Empresa')
