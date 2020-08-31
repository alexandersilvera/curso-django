from django.urls import path

from pypro.blog import views

app_name = 'blog'
urlpatterns = [
    path(
        '',
        views.EntryListView.as_view(),
        name='entradas',
    ),
    path(
        'blog/<pk>/',
        views.EntryDetailView.as_view(),
        name='entry-detail',
    ),
]
