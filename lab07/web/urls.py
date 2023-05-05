from django.urls import path

from . import views


app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('profesor/', views.ProfesorView.as_view(),name='profesor'),
    path('eliminar/<int:alumno_id>/', views.AlumnoView.eliminar, name='eliminar'),
    path('eliminar_profesor/profesor/<int:profesor_id>/', views.ProfesorView.eliminar_profesor, name='eliminar_profesor'),
]


