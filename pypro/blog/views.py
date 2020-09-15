from django.views.generic import (
    ListView,
    DetailView
)
# app
from .models import Entry, Category


class EntryListView(ListView):
    template_name = "blog/blog.html"
    context_object_name = 'entradas'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        return context

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '')
        # consulta de busqueda
        resultado = Entry.objects.buscar_entrada(kword, categoria)
        return resultado


class EntryDetailView(DetailView):
    template_name = "blog/detalle.html"
    model = Entry
