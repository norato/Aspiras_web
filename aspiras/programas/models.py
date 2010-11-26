from django.db import models


class Exercicio1(models.Model):

    valor = models.IntegerField()

class Exercicio2(models.Model):

    valor = models.IntegerField()

class Exercicio3(models.Model):

    valor1 = models.IntegerField()
    valor2 = models.IntegerField()
    valor3 = models.IntegerField()

class Exercicio4(models.Model):

    valor = models.IntegerField()

class Exercicio5(models.Model):

    taxa_do_imposto = models.IntegerField()
    custo = models.IntegerField()

class Exercicio6(models.Model):

    hora = models.IntegerField()
    minuto = models.IntegerField()

class Exercicio8(models.Model):

    numero = models.IntegerField()

class Exercicio9(models.Model):

    numero = models.IntegerField()

class Exercicio10(models.Model):

    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()

