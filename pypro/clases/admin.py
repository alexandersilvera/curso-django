from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
# Register your models here.
from pypro.clases.models import Clase

=======
from pypro.clases.models import Clase


>>>>>>> 37f9113f5b4019ee76cba69763aab8d0c83c302b
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'inicio', 'fin')
    prepopulated_fields = {'slug': ('nombre',)}
<<<<<<< HEAD
    ordering = ('-inicio',)
=======
    ordering = ('-inicio',)
>>>>>>> 37f9113f5b4019ee76cba69763aab8d0c83c302b
