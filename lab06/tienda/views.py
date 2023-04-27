from django.shortcuts import get_object_or_404, render

from .models import Producto, Categoria
# Create your views here.


def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria_lista = Categoria.objects.all()
    context = {
        'product_list': product_list,
        'categorias': categoria_lista
    }

    return render(request, 'index.html', context)


def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categoria_lista = Categoria.objects.all()
    context = {
        'producto': producto,
        'categorias': categoria_lista
    }
    return render(request, 'producto.html', context)


"""
def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html',  {'producto': producto})
"""


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    product_list = categoria.producto_set.all()
    categoria_lista = Categoria.objects.all()

    context = {
        'product_list': product_list,
        'categorias': categoria_lista
    }
    return render(request, 'index.html', context)
