from django.db import models


class Exercicio1(models.Model):

    valor = models.IntegerField()

class Exercicio2(models.Model):

    valor = models.IntegerField()

class Exercicio3(models.Model):

    valor1 = models.IntegerField()
    valor2 = models.IntegerField()
    valor3 = models.IntegerField()

class Exercicio7(models.Model):

    valor_prestacao = models.IntegerField()
    numero_prestacoes = models.IntegerField()

class Exercicio10(models.Model):

    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()

