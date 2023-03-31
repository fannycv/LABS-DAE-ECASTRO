from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'titulo': "CÁLCULO DEL VOLUMEN DE UN CILINDRO",
    }
    return render(request, 'cilindro/formulario.html', context)


def calcular(request):
    altura = float(request.POST['altura'])
    diametro = float(request.POST['diametro'])
    radio = diametro / 2
    volumen = round(altura * 3.1416 * radio ** 2, 4)
    context = {
        'titulo': 'Resultado del cálculo',
        'altura': altura,
        'diametro': diametro,
        'volumen': volumen,
    }
    return render(request, 'cilindro/resultado.html', context)
