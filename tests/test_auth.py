import pytest

from jeru import create_app
from jeru.blueprints.auth.controllers import (create_user, delete_user,
                                              get_all_users, get_user_by_id,
                                              make_login, update_user)
from jeru.ext.db import init_app


@pytest.fixture
def client():
    app = create_app()
    with app.app_context():
        init_app(app)
        yield app


def test_create_user(client):
    data = {
        "id": 2,
        "username": "user_test",
        "email": "test@gmail.com",
        "birthday": "14/12/1999",
        "password": "1234test",
    }
    user = create_user(data)
    assert user.username == "user_test"
    assert user.email == "test@gmail.com"


def test_get_users(client):
    users = get_all_users()
    assert users[0].username in ("Lnvictor", "user_test")


def test_get_user_by_id(client):
    user = get_user_by_id(1)
    assert user.username == "Lnvictor"


def test_update_user(client):
    user = update_user(2, {"username": "fuba"})
    assert user.username == "fuba"


def test_delete_user(client):
    assert delete_user(2)
