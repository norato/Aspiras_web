from django import forms
from models import Exercicio1, Exercicio2, Exercicio3, Exercicio7, Exercicio10

class Exercicio1Form(forms.ModelForm):
    class Meta:

        model = Exercicio1

class Exercicio2Form(forms.ModelForm):
    class Meta:

        model = Exercicio2

class Exercicio3Form(forms.ModelForm):
    class Meta:

        model = Exercicio3

class Exercicio7Form(forms.ModelForm):
    class Meta:

        model = Exercicio7

class Exercicio10Form(forms.ModelForm):
    class Meta:

        model = Exercicio10

