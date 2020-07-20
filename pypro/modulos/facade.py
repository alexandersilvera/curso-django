from typing import List

from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por titulos
    """
    return list(Modulo.objects.order_by('order').all())
