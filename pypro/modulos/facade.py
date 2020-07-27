from typing import List

from django.db.models import Prefetch

from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por paramento order
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulos_ordenados(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
<<<<<<< HEAD
    return Aula.objects.get(slug=slug)
=======
    return Aula.objects.select_related('modulo').get(slug=slug)
>>>>>>> 37f9113f5b4019ee76cba69763aab8d0c83c302b


def listar_modulos_con_aulas():
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(
        Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')
    ).all()
