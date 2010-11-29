from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import Exercicio1Form, Exercicio2Form, Exercicio3Form, \
                    Exercicio4Form, Exercicio5Form, Exercicio6Form, Exercicio8Form, Exercicio9Form, Exercicio10Form, Exercicio11Form, Exercicio12Form, Exercicio13Form, Exercicio14Form, Exercicio15Form, Exercicio16Form, Exercicio17Form, Exercicio18Form, Exercicio19Form
#                    Exercicio7Form,
from programas.exe1 import Numero, Data, Dinheiro, Medida, Palavra



def lista(request):
    return render_to_response(
        'pag.html'
        )

def exercicio1(request):
    exercicio1_form = Exercicio1Form()
    if request.method == 'POST':
        exercicio1_form = Exercicio1Form(request.POST)
        if exercicio1_form.is_valid():
            valor = request.POST.get('valor')
            resultado = Numero(int(valor)).programa1
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
            resultado = Numero(int(valor)).programa2
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
            resultado = Numero().programa3(int(valor1) ,int(valor2) ,int(valor3))
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

def exercicio4(request):
    exercicio4_form = Exercicio4Form()
    if request.method == 'POST':
        exercicio4_form = Exercicio4Form(request.POST)
        if exercicio4_form.is_valid():
            valor = request.POST.get('valor')
            resultado = Numero(int(valor)).programa4
            return render_to_response(
                'exercicio4.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio4.html',
            {'exercicio4_form': exercicio4_form},
            context_instance=RequestContext(request)
            )

def exercicio5(request):
    exercicio5_form = Exercicio5Form()
    if request.method == 'POST':
        exercicio5_form = Exercicio5Form(request.POST)
        if exercicio5_form.is_valid():
            taxa_do_imposto = request.POST.get('taxa_do_imposto')
            custo = request.POST.get('custo')
            resultado = Dinheiro().programa5(float(taxa_do_imposto),float(custo))
            return render_to_response(
                'exercicio5.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio5.html',
            {'exercicio5_form': exercicio5_form},
            context_instance=RequestContext(request)
            )

def exercicio6(request):
    exercicio6_form = Exercicio6Form()
    if request.method == 'POST':
        exercicio6_form = Exercicio6Form(request.POST)
        if exercicio6_form.is_valid():
            hora = request.POST.get('hora')
            minuto = request.POST.get('minuto')
            resultado = Numero(int(hora)).programa6(int(minuto))
            return render_to_response(
                'exercicio6.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio6.html',
            {'exercicio6_form': exercicio6_form},
            context_instance=RequestContext(request)
            )

def exercicio8(request):
    exercicio8_form = Exercicio8Form()
    if request.method == 'POST':
        exercicio8_form = Exercicio8Form(request.POST)
        if exercicio8_form.is_valid():
            numero = request.POST.get('numero')
            resultado = Numero(int(numero)).programa8
            return render_to_response(
                'exercicio8.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio8.html',
            {'exercicio8_form': exercicio8_form},
            context_instance=RequestContext(request)
            )

def exercicio9(request):
    exercicio9_form = Exercicio9Form()
    if request.method == 'POST':
        exercicio9_form = Exercicio9Form(request.POST)
        if exercicio9_form.is_valid():
            numero = request.POST.get('numero')
            resultado = Numero(int(numero)).programa9
            return render_to_response(
                'exercicio9.html',
                {'resultado': resultado},
                context_instance=RequestContext(request)
            )
    return render_to_response(
            'exercicio9.html',
            {'exercicio9_form': exercicio9_form},
            context_instance=RequestContext(request)
            )

def exercicio10(request):
    exercicio10_form = Exercicio10Form()
    if request.method == 'POST':
        exercicio10_form = Exercicio10Form(request.POST)
        if exercicio10_form.is_valid():
            dia = request.POST.get('dia')
            mes = request.POST.get('mes')
            ano = request.POST.get('ano')
            resultado = Data().programa10(int(dia), int(mes), int(ano))
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
def exercicio11(request):
    exercicio11_form = Exercicio11Form()
    if request.method == 'POST':
        exercicio11_form = Exercicio11Form(request.POST)
        if exercicio11_form.is_valid():
            palavra = request.POST.get('palavra')
            resultado = Palavra(palavra).programa11
            return render_to_response(
                'exercicio11.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio11.html',
            {'exercicio11_form': exercicio11_form},
            context_instance = RequestContext(request)
    )

def exercicio12(request):
    exercicio12_form = Exercicio12Form()
    if request.method == 'POST':
        exercicio12_form = Exercicio12Form(request.POST)
        if exercicio12_form.is_valid():
            medida1 = request.POST.get('medida1')
            medida2 = request.POST.get('medida2')
            resultado = Medida(int(medida1)).programa12(int(medida2))
            return render_to_response(
                'exercicio12.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio12.html',
            {'exercicio12_form': exercicio12_form},
            context_instance = RequestContext(request)
    )

def exercicio13(request):
    exercicio13_form = Exercicio13Form()
    if request.method == 'POST':
        exercicio13_form = Exercicio13Form(request.POST)
        if exercicio13_form.is_valid():
            palavra1 = request.POST.get('palavra1')
            palavra2 = request.POST.get('palavra2')
            resultado = Palavra(palavra1).programa13(palavra2)
            return render_to_response(
                'exercicio13.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio13.html',
            {'exercicio13_form': exercicio13_form},
            context_instance = RequestContext(request)
    )


def exercicio14(request):
    exercicio14_form = Exercicio14Form()
    if request.method == 'POST':
        exercicio14_form = Exercicio14Form(request.POST)
        if exercicio14_form.is_valid():
            nome = request.POST.get('nome')
            resultado = Palavra(nome).programa14
            return render_to_response(
                'exercicio14.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio14.html',
            {'exercicio14_form': exercicio14_form},
            context_instance = RequestContext(request)
    )

def exercicio15(request):
    exercicio15_form = Exercicio15Form()
    if request.method == 'POST':
        exercicio15_form = Exercicio15Form(request.POST)
        if exercicio15_form.is_valid():
            nome = request.POST.get('nome')
            resultado = Palavra(nome).programa15
            return render_to_response(
                'exercicio15.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio15.html',
            {'exercicio15_form': exercicio15_form},
            context_instance = RequestContext(request)
    )

def exercicio16(request):
    exercicio16_form = Exercicio16Form()
    if request.method == 'POST':
        exercicio16_form = Exercicio16Form(request.POST)
        if exercicio16_form.is_valid():
            nome = request.POST.get('nome')
            resultado = Palavra(nome).programa16
            return render_to_response(
                'exercicio16.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio16.html',
            {'exercicio16_form': exercicio16_form},
            context_instance = RequestContext(request)
    )

def exercicio17(request):
    exercicio17_form = Exercicio17Form()
    if request.method == 'POST':
        exercicio17_form = Exercicio17Form(request.POST)
        if exercicio17_form.is_valid():
            nome = request.POST.get('nome')
            resultado = Palavra(nome).programa17
            return render_to_response(
                'exercicio17.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio17.html',
            {'exercicio17_form': exercicio17_form},
            context_instance = RequestContext(request)
    )

def exercicio18(request):
    exercicio18_form = Exercicio18Form()
    if request.method == 'POST':
        exercicio18_form = Exercicio18Form(request.POST)
        if exercicio18_form.is_valid():
            frase = request.POST.get('frase1')
            resultado = Palavra(frase).programa18
            return render_to_response(
                'exercicio18.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio18.html',
            {'exercicio18_form': exercicio18_form},
            context_instance = RequestContext(request)
    )

def exercicio19(request):
    exercicio19_form = Exercicio19Form()
    if request.method == 'POST':
        exercicio19_form = Exercicio19Form(request.POST)
        if exercicio19_form.is_valid():
            frase = request.POST.get('frase')
            resultado = Palavra(frase).programa19
            return render_to_response(
                'exercicio19.html',
                {'resultado': resultado},
                context_instance = RequestContext(request)
            )
    return render_to_response(
            'exercicio19.html',
            {'exercicio19_form': exercicio19_form},
            context_instance = RequestContext(request)
    )

