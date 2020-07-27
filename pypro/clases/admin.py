from django.contrib import admin

# Register your models here.
# Register your models here.
from pypro.clases.models import Clase

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'inicio', 'fin')
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ('-inicio',)