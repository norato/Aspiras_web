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
class Exercicio7(models.Model):
    pass

class Exercicio8(models.Model):

    numero = models.IntegerField()

class Exercicio9(models.Model):

    numero = models.IntegerField()

class Exercicio10(models.Model):

    dia = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()

class Exercicio11(models.Model):

    palavra = models.CharField(max_length ='200')

class Exercicio12(models.Model):

    medida1 = models.IntegerField()
    medida2 = models.IntegerField()

class Exercicio13(models.Model):

    palavra1 = models.CharField(max_length ='1000')
    palavra2 = models.CharField(max_length ='1000')

class Exercicio14(models.Model):

    nome = models.CharField(max_length = '200')

class Exercicio15(models.Model):

    nome = models.CharField(max_length = '200')

class Exercicio16(models.Model):

    nome = models.CharField(max_length = '200')

class Exercicio17(models.Model):

    nome = models.CharField(max_length = '200')

class Exercicio18(models.Model):

    frase1 = models.CharField(max_length = '1000')

class Exercicio19(models.Model):

    frase = models.CharField(max_length = '1000')

