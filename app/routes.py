from flask import render_template
from app import app, db
from sqlalchemy.sql import func
from app.models import measurements

@app.route('/')
@app.route('/index')
def index():
    try:
        query = db.session.query(func.max(measurements.timestamp))
        newest_timestamp = query.one()
        query2 = db.session.query(measurements).filter(measurements.timestamp == newest_timestamp)
        m = query2.one()
        cloudy_limit = 600
        sunny_limit = 1000
        cloudy_text = ""
        if m.ill > sunny_limit:
            cloudy_text = "Sunny"
        elif m.ill < cloudy_limit:
            cloudy_text = "Cloudy"
        else:
            cloudy_text = "Partly Cloudy"
        return render_template('index.html', measurement=m, is_cloudy=cloudy_text)
    except:
        return render_template('error.html', errormessage="Cant'retreve data")
