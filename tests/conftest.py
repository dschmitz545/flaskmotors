import pytest

from flaskmotors.app import create_app


@pytest.fixture(scope="module")
def app():
    """ Instânciando o módulo main do flask app """
    return create_app()
