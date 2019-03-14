from requests_html import HTMLSession
import re
import time
import locale
import datetime

def get_menu():
    session = HTMLSession()
    response = session.get('https://docs.google.com/forms/d/e/1FAIpQLSc6kSPKeZNvGsRXuowis8xvDRTuaGEPDYFI9mehp3GWALLbTg/viewform')
    description = response.html.find('.freebirdFormviewerViewHeaderDescription')[0].text
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'viernes']
    regex = re.compile('(\w+ [0-9]+ \w+\.)\n([^\n]+)')
    match = regex.findall(description)
    #print(match)print(date_result)
    menu = {}
    for menu_item in match:
        item = parse_menu_item(menu_item)
        menu[item[0]] = item[1]
    return menu



def parse_menu_item(menu_item):
    date_format = '%A %d %b'
    locale.setlocale(locale.LC_TIME, 'es_ES')
    current_date = datetime.date.today()
    #print(menu_item[0])
    date = datetime.datetime.strptime(menu_item[0].strip().replace('.', '').lower().replace('miercoles', 'miércoles'), date_format).date().replace(year=current_date.year)
    return (date, menu_item[1])
