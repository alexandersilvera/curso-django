import pytest
from model_mommy import mommy


@pytest.fixture
def usuario_logeado(db, django_user_model):
    usuario_modelo = mommy.make(django_user_model, first_name='Fulano')
    return usuario_modelo


@pytest.fixture
def client_con_usuario_logeado(usuario_logeado, client):
    client.force_login(usuario_logeado)
    return client
