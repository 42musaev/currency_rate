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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        currency = {
            'USD': 'R01235',
            'EUR': 'R01239',
        }
        return render_template('app/index.html', currency=currency)

    elif request.method == 'POST':
        date_req1 = request.form['date_req1']
        date_req2 = request.form['date_req2']
        currency = request.form['currency']
        if date_req1 and date_req2 and currency:
            url = "http://www.cbr.ru/scripts/XML_dynamic.asp?"
            params = {
                'date_req1': datetime.strptime(date_req1, "%Y-%m-%d").strftime("%d-%m-%Y"),
                'date_req2': datetime.strptime(date_req2, "%Y-%m-%d").strftime("%d-%m-%Y"),
                'VAL_NM_RQ': currency
            }
            r = requests.get(url, params)
            data = xml_to_dict(r.text)
            return f"{data}"
        return 200
