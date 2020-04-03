from flask import render_template
from app import app, db
from sqlalchemy.sql import func
from app.models import measurements

@app.route('/')
@app.route('/index')
def index():
    query = db.session.query(func.max(measurements.timestamp))
    newest_timestamp = query.one()
    query2 = db.session.query(measurements).filter(measurements.timestamp == newest_timestamp)
    m=query2.one()
    return render_template('index.html', measurement=m)
