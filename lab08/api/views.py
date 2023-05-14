from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from tienda.models import Categoria, Producto
from series.models import Serie
from .serializers import CategoriaSerializer, ProductoSerializer, SerieSerializer


class IndexView(APIView):
    def get(self, request):
        lista_series = Serie.objects.all()
        serializer_serie = SerieSerializer(lista_series, many=True)

        lista_categorias = Categoria.objects.all()
        serializer_categoria = CategoriaSerializer(lista_categorias, many=True)

        lista_productos = Producto.objects.all()
        serializer_producto = ProductoSerializer(lista_productos, many=True)

        data = {
            "series": serializer_serie.data,
            "categorias": serializer_categoria.data,
            "productos": serializer_producto.data,
        }

        return Response(data)


class SeriesView(APIView):
    def get(self, request):
        dataSeries = Serie.objects.all()
        serSeries = SerieSerializer(dataSeries, many=True)
        return Response(serSeries.data)

    def post(self, request):
        serSerie = SerieSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()

        return Response(serSerie.data)


class SerieDetailView(APIView):
    def get(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        return Response(serSerie.data)

    def put(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie, data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)

    def delete(self, request, serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        serSerie = SerieSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)


class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg = "categoria_id"
    serializer_class = CategoriaSerializer


class ProductoView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    lookup_url_kwarg = "producto_id"
    serializer_class = ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
