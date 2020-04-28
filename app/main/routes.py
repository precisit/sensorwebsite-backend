from flask import render_template
from app import db
from sqlalchemy.sql import func
from app.models import measurements
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    try:
        query = db.session.query(func.max(measurements.timestamp))
        newest_timestamp = query.one()
        query2 = db.session.query(measurements).filter(measurements.timestamp == newest_timestamp)
        m = query2.one()
        cloudy_text = get_cloud_text(m.ill)
        return render_template('index.html', measurement=m, is_cloudy=cloudy_text)
    except:
        return render_template('error.html')


def get_cloud_text(ill):
    cloudy_text = ""
    cloudy_limit = 530
    sunny_limit = 1100
    if ill > sunny_limit:
        cloudy_text = "Sunny"
    elif ill < cloudy_limit:
        cloudy_text = "Cloudy"
    else:
        cloudy_text = "Partly Cloudy"
    return cloudy_text
