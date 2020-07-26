from django.urls import path

from pypro.clases import views

app_name = 'clases'
urlpatterns = [
    path('', views.indice, name='indice'),
]
