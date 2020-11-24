from app import app, db
from flask import render_template, request, redirect, url_for
import requests
from datetime import datetime
from app import cache
from .utils import xml_to_dict
from app.models import CurrencyRate, Currency
import json


def get_currency(f_date, b_date, c):
    url = "http://www.cbr.ru/scripts/XML_dynamic.asp?"
    f_date = datetime.strptime(f_date, "%Y-%m-%d").strftime("%d-%m-%Y"),
    b_date = datetime.strptime(b_date, "%Y-%m-%d").strftime("%d-%m-%Y"),
    params = {
        'date_req1': f_date,
        'date_req2': b_date,
        'VAL_NM_RQ': c,
    }
    r = requests.get(url, params)
    return r.text


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        currency = Currency.query.all()
        return render_template('app/index.html', currency=currency)

    elif request.method == 'POST':
        date_req1 = request.form.get('date_req1', False)
        date_req2 = request.form.get('date_req2', False)
        currency = request.form.get('currency', False)

        if date_req1 and date_req2 and currency:
            xml = get_currency(date_req1, date_req2, currency)
            data = xml_to_dict(xml)
            full_data = {
                'currency': currency,
                'data': data,
                'from_date': date_req1,
                'before_date': date_req2,
            }
            cache.set('full_data', full_data)
            return render_template('app/prev.html', full_data=full_data)

        elif request.form.get('save', False):
            full_data = cache.get('full_data')
            if full_data:
                data = json.dumps(full_data['data'], indent=4)
                currency = Currency.query.filter(
                    Currency.code==full_data['currency']
                    ).first()

                cr = CurrencyRate(
                    data=data,
                    time_from=full_data['from_date'],
                    time_before=full_data['before_date'],
                    currency_id=currency.id
                )
                db.session.add(cr)
                db.session.commit()
                return redirect(url_for('detail', currency_id=cr.id))
            return redirect(url_for('index'))

        else:
            errors = {
                "error": "incorrect data entry"
            }
        return render_template('app/index.html', errors=errors)


@app.route('/list')
def list():
    if request.method == 'GET':
        crs = CurrencyRate.query.all()
        return render_template('app/list.html', currency=crs)


@app.route('/cr/<currency_id>')
def detail(currency_id):
    currency = CurrencyRate.query.filter(CurrencyRate.id==currency_id).first()
    return render_template('app/detail.html', currency=currency)
