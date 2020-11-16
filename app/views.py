from app import app
from flask import render_template, request
import requests
from datetime import datetime
import xml.etree.ElementTree as ET


def xml_to_dict(xml):
    root = ET.fromstring(xml)
    result = []
    for record in root.findall('Record'):
        date = record.get('Date')
        value = record.find('Value').text
        result.append({'date': date, 'value': value})
    return result


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
        currency = {
            'USD': 'R01235',
            'EUR': 'R01239',
        }
        return render_template('app/index.html', currency=currency)

    elif request.method == 'POST':
        date_req1 = request.form.get('date_req1', False)
        date_req2 = request.form.get('date_req2', False)
        currency = request.form.get('currency', False)

        if date_req1 and date_req2 and currency:
            xml = get_currency(date_req1, date_req2, currency)
            data = xml_to_dict(xml)
            return render_template('app/detail.html', data=data)

        elif request.form.get('save', False):
            return '200'
        else:
            errors = {
                "error": "incorrect data entry"
            }
        return render_template('app/detail.html', errors=errors)
