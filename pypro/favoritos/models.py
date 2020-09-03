from django.contrib.auth import get_user_model
from django.db import models
# apps terceros
from model_utils.models import TimeStampedModel
#
from pypro.blog.models import Entry
#
from .managers import FavoritesManager


class Favorites(TimeStampedModel):
    """ Modelo para Favoritos """
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()

    class Meta:
        unique_together = ('usuario', 'entry')
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'

    def __str__(self):
        return self.entry.title
