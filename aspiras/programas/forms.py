from django import forms
from models import Exercicio1, Exercicio2, Exercicio3, Exercicio4, Exercicio5, Exercicio6, Exercicio8, Exercicio9, Exercicio10
#                    , Exercicio7,  

class Exercicio1Form(forms.ModelForm):
    class Meta:

        model = Exercicio1

class Exercicio2Form(forms.ModelForm):
    class Meta:

        model = Exercicio2

class Exercicio3Form(forms.ModelForm):
    class Meta:

        model = Exercicio3

class Exercicio4Form(forms.ModelForm):
    class Meta:

        model = Exercicio4

class Exercicio5Form(forms.ModelForm):
    class Meta:

        model = Exercicio5

class Exercicio6Form(forms.ModelForm):
    class Meta:

        model = Exercicio6

#class Exercicio7Form(forms.ModelForm):
#    class Meta:

#        model = Exercicio7

class Exercicio8Form(forms.ModelForm):
    class Meta:

        model = Exercicio8

class Exercicio9Form(forms.ModelForm):
    class Meta:

        model = Exercicio9

class Exercicio10Form(forms.ModelForm):
    class Meta:

        model = Exercicio10

