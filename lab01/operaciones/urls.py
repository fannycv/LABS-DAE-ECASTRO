from django.urls import path


from . import views


urlpatterns = [

    # ex: localhost:8000/app/
    path('', views.index, name='index'),

    # ex: localhost:8000/app/sumar/18/19/
    path('sumar/<int:num1>/<int:num2>/', views.suma, name='suma'),

    # ex: localhost:8000/app/restar/18/19/
    path('restar/<int:num1>/<int:num2>/', views.resta, name='resta'),

    # ex: localhost:8000/app/multiplicar/num1/num2/
    path('multiplicar/<int:num1>/<int:num2>/',
         views.multiplicacion, name='multiplicacion'),
]
