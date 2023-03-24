from django.http import HttpResponse


def index(request):
    return HttpResponse("Desde la vista de operaciones!")


def suma(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f"La suma de {num1} + {num2} = {result}")


def resta(request, num1, num2):
    result = num1 - num2
    return HttpResponse(f"La resta de {num1} - {num2} = {result}")


def multiplicacion(request, num1, num2):
    result = num1 * num2
    return HttpResponse(f"La multiplicacion de {num1} x {num2} = {result}")
