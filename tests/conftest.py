import pytest

from easyagro.gateway import create_app
from easyagro.gateway.extensions import db as _db


@pytest.fixture
def app():
    app = create_app(config='easyagro.gateway.config.Testing')
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
