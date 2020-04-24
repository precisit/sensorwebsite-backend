import os
import tempfile
import datetime
import pytest
from config import Config
from app.models import measurements
from app import create_app, db


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        yield client



def test_index(client):
    rv = open_root(client)
    assert b'Uppsala' in rv.data
    assert b'Sweden' in rv.data


@pytest.mark.skip("WIP")
def test_date(client):
    rv = open_root(client)
    t = datetime.datetime.now()
    day_name = [b'Monday', b'Tuesday', b'Wednesday', b'Thursday', b'Friday', b'Saturday', b'Sunday']
    assert day_name[t.weekday()] in rv.data


def open_root(client):
    return client.get('/')
