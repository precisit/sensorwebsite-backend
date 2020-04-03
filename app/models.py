from app import db
from datetime import datetime


class measurements(db.Model):
    timestamp = db.Column(db.String, primary_key=True)
    year = db.Column(db.Integer, index=True)
    month = db.Column(db.Integer, index=True)
    day = db.Column(db.Integer, index=True)
    hour = db.Column(db.Integer, index=True)
    minute = db.Column(db.Integer, index=True)
    second = db.Column(db.Integer, index=True)
    temp = db.Column(db.Float, index=True)
    hum = db.Column(db.Float, index=True)
    pres = db.Column(db.Float, index=True)
    ill = db.Column(db.Float, index=True)
    uv = db.Column(db.Float, index=True)

    def followed_posts(self):
        return measurements.query(User).filter_by(name='ed').first()
    def __repr__(self):
        return '<Measurements, timestamp {}>'.format(self.timestamp)