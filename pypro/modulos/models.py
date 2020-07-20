from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=65)
    publico = models.TextField()
    descripcion = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalle', kwargs={'slug': self.slug})
