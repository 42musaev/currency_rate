from app import db
from datetime import datetime


class CurrencyRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(256))
    data = db.Column(db.JSON)
    time_from = db.Column(db.DateTime)
    time_before = db.Column(db.DateTime)
    created = db.Column(db.DateTime, default=datetime.now())
