from app import create_app, db
from app.models import measurements
from config import Config
import unittest
import os
from sqlalchemy.sql import func
basedir = os.path.abspath(os.path.dirname(__file__))

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'app.db')


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_db_connection(self):
        db.session.query(measurements).get(1)
        assert 'sqlite://' in self.app.config['SQLALCHEMY_DATABASE_URI']

    def test_get_max(self):
        m_new = measurements(timestamp='12345678', year=2020, month=2, day=3, hour=3, minute=2, second=4, temp=20, hum=3, pres=4, ill=4, uv=4)
        m_old = measurements(timestamp='1234', year=2020, month=2, day=3, hour=3, minute=2, second=4, temp=20, hum=3, pres=4, ill=4, uv=4)
        db.session.add(m_new)
        db.session.add(m_old)
        db.session.commit()
        #query = db.session.query(func.max(measurements.timestamp))
        #newest_timestamp = query.one()
        #query2 = db.session.query(measurements).filter(measurements.timestamp == newest_timestamp)
        #m = query2.one()
        #assert m.timestamp == '12345678'


if __name__ == '__main__':
    unittest.main()