from django.urls import path

from pypro.favoritos import views

app_name = 'favoritos'
urlpatterns = [
    path(
        'perfil/',
        views.UserPageView.as_view(),
        name='perfil',
    ),
    path(
        'add-entrada/<pk>/',
        views.AddFavoritosView.as_view(),
        name='add-favoritos',
    ),
    path(
        'delete-favorites/<pk>/',
        views.FavoritesDeleteView.as_view(),
        name='delete-favoritos',
    ),
]
