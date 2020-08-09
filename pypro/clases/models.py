from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fin = models.DateField()
    alumnos = models.ManyToManyField(get_user_model(), through='Matricula')


class Matricula(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['usuario', 'clase']]
        ordering = ['clase', 'data']
