from django.contrib import admin

# Register your models here.

from pypro.clases.models import Clase

class MatriculaInline(admin.TabularInline):
    model = Clase.alumnos.through
    extra = 1
    readonly_fields = ('data',)
    autocomplete_fields = ('usuario',)
    ordering = ('-data',)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]
    list_display = ('nombre', 'slug', 'inicio', 'fin')
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ('-inicio',)
