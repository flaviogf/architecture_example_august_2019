import pytest

from easyagro.gateway import create_app


@pytest.fixture
def app():
    app = create_app(config='easyagro.gateway.config.Testing')
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()
