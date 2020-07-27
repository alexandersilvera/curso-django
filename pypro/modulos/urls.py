from django.urls import path

from pypro.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalle, name='detalle'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
    path('', views.indice, name='indice'),
]
