import xml.etree.ElementTree as ET


def xml_to_dict(xml):
    root = ET.fromstring(xml)
    result = []
    for record in root.findall('Record'):
        date = record.get('Date')
        value = record.find('Value').text
        result.append({'date': date, 'value': value})
    return result
