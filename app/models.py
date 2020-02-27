from app import db
from datetime import datetime


class Temperature(db.Model):
    #t = datetime.today()
    timestamp = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)
    #year = db.Column(db.Integer, index=True, default=t.year)
    #month = db.Column(db.Integer, index=True, default=t.month)
    #day = db.Column(db.Integer, index=True, default=t.day)
    #hour = db.Column(db.Integer, index=True, default=t.hour)
    #minute = db.Column(db.Integer, index=True, default=t.minute)
    #second = db.Column(db.Integer, index=True, default=t.second)
    value = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Measurement {}>'.format(self.value)


class Humidity(db.Model):
    #t = datetime.today()
    timestamp = db.Column(db.DateTime, primary_key=True, default=datetime.utcnow)
    #year = db.Column(db.Integer, index=True, default=t.year)
    #month = db.Column(db.Integer, index=True, default=t.month)
    #day = db.Column(db.Integer, index=True, default=t.day)
    #hour = db.Column(db.Integer, index=True, default=t.hour)
    #minute = db.Column(db.Integer, index=True, default=t.minute)
    #second = db.Column(db.Integer, index=True, default=t.second)
    value = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Measurement {}>'.format(self.value)
