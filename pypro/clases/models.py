from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    inicio = models.DateField()
    fin = models.DateField()
    matriculas = models.ManyToManyField(get_user_model())
