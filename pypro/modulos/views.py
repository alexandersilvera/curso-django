from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pypro.modulos import facade


def indice(request):
    ctx = {'modulos': facade.listar_modulos_con_aulas()}
    return render(request, 'modulos/indice.html', ctx)


def detalle(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalle.html', {'modulo': modulo, 'aulas': aulas})

@login_required
def aula(request, slug):
    aula = facade.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalle.html', {'aula': aula})
