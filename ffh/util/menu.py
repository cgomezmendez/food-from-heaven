from requests_html import HTMLSession
import re
import time
import locale
import datetime


def get_menu_info():
    return """
    semana del 18  al
22 de Mar. 2019.

Lunes 18 Mar.
Sin seevicios

Martes 19 Mar.
Chili con carne, arroz blanco, ensalada pico de gallo y nachos

Miercoles 20 Mar.
Arroz cin maiz, muslos de pollo al horno, ensalada y fritura.

Jueves 21 Mar.
Spaghetti en salsa Alfredo con trozos de chuletas ahumadas y tostadas con manrequilla de ajo.

viernes 22 Mar.
Chofan Mixto, Eggs roll, ensalada
    """

def get_menu():
    #session = HTMLSession()
    #response = session.get('https://docs.google.com/forms/d/e/1FAIpQLSc6kSPKeZNvGsRXuowis8xvDRTuaGEPDYFI9mehp3GWALLbTg/viewform')
    #description = response.html.find('.freebirdFormviewerViewHeaderDescription')[0].text
    description = get_menu_info()
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'viernes']
    regex = re.compile('(\w+ [0-9]+ \w+\.)\n([^\n]+)')
    match = regex.findall(description)
    #print(match)print(date_result)
    menu = {}
    for menu_item in match:
        item = parse_menu_item(menu_item)
        menu[item[0]] = item[1]
    print(menu)
    return menu



def parse_menu_item(menu_item):
    date_format = '%A %d %b'
    locale.setlocale(locale.LC_TIME, 'es_ES')
    current_date = datetime.date.today()
    #print(menu_item[0])
    date = datetime.datetime.strptime(menu_item[0].strip().replace('.', '').lower().replace('miercoles', 'miércoles'), date_format).date().replace(year=current_date.year)
    return (date, menu_item[1])
