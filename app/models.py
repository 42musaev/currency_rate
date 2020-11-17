from app import db
from datetime import datetime


class CurrencyRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)
    time_from = db.Column(db.DateTime)
    time_before = db.Column(db.DateTime)
    created = db.Column(db.DateTime, default=datetime.now())
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship("Currency", backref=db.backref("currency", uselist=False))


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    code = db.Column(db.String(256), unique=True)

    def __repr__(self):
        return self.name
