from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'titulo': "Formulario de operaciones",
    }
    return render(request, 'calculadora/formulario.html', context)


def calcular(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        operacion = request.POST['operacion']

        if operacion == 'suma':
            respuesta = num1 + num2
            signo = '+'
        elif operacion == 'resta':
            respuesta = num1 - num2
            signo = '-'
        elif operacion == 'multiplicacion':
            respuesta = num1 * num2
            signo = 'x'

        context = {
            'num1': num1,
            'num2': num2,
            'operacion': operacion,
            'signo': signo,
            'respuesta': respuesta,
        }

        return render(request, 'calculadora/respuesta.html', context)
