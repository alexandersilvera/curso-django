import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = mommy.make(django_user_model)
    contrasena = 'contrasena'
    usuario_modelo.set_password(contrasena)
    usuario_modelo.save()
    usuario_modelo.contrasena_plana = contrasena
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.contrasena_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_boton_entrar_disponible(resp_home):
    assert_contains(resp_home, 'Entrar')


def test_link_de_login_disponible(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_con_usuario_logeado(client_con_usuario_logeado, db):
    return client_con_usuario_logeado.get(reverse('base:home'))


def test_boton_entrar_indisponible(resp_home_con_usuario_logeado):
    assert_not_contains(resp_home_con_usuario_logeado, 'Entrar')


def test_link_de_login_indisponible(resp_home_con_usuario_logeado):
    assert_not_contains(resp_home_con_usuario_logeado, reverse('login'))


def test_boton_salir_disponible(resp_home_con_usuario_logeado):
    assert_contains(resp_home_con_usuario_logeado, 'Salir')


def test_nombre_usuario_logeado_disponible(resp_home_con_usuario_logeado, usuario_logeado):
    assert_contains(resp_home_con_usuario_logeado, usuario_logeado.first_name)


def test_link_de_logout_disponible(resp_home_con_usuario_logeado):
    assert_contains(resp_home_con_usuario_logeado, reverse('logout'))
