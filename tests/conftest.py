import pytest

from easyagro import create_app
from easyagro.extensions import db as _db


@pytest.fixture
def app():
    app = create_app('easyagro.config.Testing')

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    return _db
