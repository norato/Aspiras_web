from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import Exercicio1Form, Exercicio2Form, Exercicio3Form, Exercicio7Form, Exercicio10Form
from programas.exe1 import Numero
from programas.exe2 import Numero_2
from programas.exe3 import Numero_3
from programas.exe7 import Valor
from programas.exe10 import Data



def lista(request):
    return render_to_response(
        'pag.html'
        )

def exercicio1(request):
#    import pdb; pdb.set_trace()
    exercicio1_form = Exercicio1Form()
    if request.method == 'POST':
        exercicio1_form = Exercicio1Form(request.POST)
        if exercicio1_form.is_valid():
            valor = request.POST.get('valor')
            resultado = Numero(int(valor)).teste()
            return render_to_response(
                'exercicio1.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio1.html',
            {'exercicio1_form': exercicio1_form},
            context_instance=RequestContext(request)
            )

def exercicio2(request):
    exercicio2_form = Exercicio2Form()
    if request.method == 'POST':
        exercicio2_form = Exercicio2Form(request.POST)
        if exercicio2_form.is_valid():
            valor = request.POST.get('valor')
            resultado = Numero_2(int(valor)).teste()
            return render_to_response(
                'exercicio2.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio2.html',
            {'exercicio2_form': exercicio2_form},
            context_instance=RequestContext(request)
            )

def exercicio3(request):
    exercicio3_form = Exercicio3Form()
    if request.method == 'POST':
        exercicio3_form = Exercicio3Form(request.POST)
        if exercicio3_form.is_valid():
            valor1 = request.POST.get('valor1')
            valor2 = request.POST.get('valor2')
            valor3 = request.POST.get('valor3')
            resultado = Numero_3().somar(int(valor1) ,int(valor2) ,int(valor3))
            return render_to_response(
                'exercicio3.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio3.html',
            {'exercicio3_form': exercicio3_form},
            context_instance=RequestContext(request)
            )

def exercicio7(request):
    exercicio7_form = Exercicio7Form()
    if request.method == 'POST':
        exercicio7_form = Exercicio7Form(request.POST)
        soma_total = 0
        if exercicio7_form.is_valid():
            valor_prestacao = float(request.POST.get('valor_prestacao'))
            numero_prestacoes = float(request.POST.get('numero_prestacoes'))
            total = Valor().programa(valor_prestacao, numero_prestacoes)
            soma_total += total
            return render_to_response(
                'exercicio7.html',
                {'total': total, 'soma_total': soma_total},
                context_instance = RequestContext(request)
            )
    return render_to_response(
        'exercicio7.html',
        {'exercicio7_form': exercicio7_form},
        context_instance = RequestContext(request)
    )

def exercicio10(request):
    exercicio10_form = Exercicio10Form()
    if request.method == 'POST':
        exercicio10_form = Exercicio10Form(request.POST)
        if exercicio10_form.is_valid():
            dia = request.POST.get('dia')
            mes = request.POST.get('mes')
            ano = request.POST.get('ano')
            resultado = Data().data_extenso(int(dia), int(mes), int(ano))
            return render_to_response(
                'exercicio10.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio10.html',
            {'exercicio10_form': exercicio10_form},
            context_instance=RequestContext(request)
            )

