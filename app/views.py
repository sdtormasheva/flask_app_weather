# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from requests import *
#from metar import Metar
import re

airports = ['ENSO', 'KBVX', 'RJDT', 'FSIA', 'YCNM', 'EGOW', 'CWBK', 'UAOO', 'KMBY', 'KOPN', 'PAMB', 'CXKA', 'K21D',
            'CYLC', 'EKAH', 'LTAR', 'RJCT', 'SKVV', 'KO69', 'YLEC', 'ETNN', 'KSPB', 'LFQQ', 'KMWL', 'EFET', 'CWQO',
            'KLNN', 'K2D5', 'YBRM', 'K9D7']

source = 'http://tgftp.nws.noaa.gov/data/observations/metar/decoded/'
temp_stop = -20
wind_stop = 5
press_stop = 995

@app.route('/')

@app.route('/index')
def parser(airport, temp_stop, wind_stop, press_stop):
    target_url = source + airport + '.TXT'
    airport_data = get(target_url).text.strip()

    print('Airport ', airport, ':', sep='')
    try:
        temp = re.search(r'[-]?(?:\d{1,2}|\d{1,2}\.\d) C', airport_data).group(0)
        if float(temp.split()[0]) < temp_stop:
            print('Attention! Temperature in airport ', airport, ' is below ', str(temp_stop), '.', sep='')
        else:
            print('Temperature in airport', airport, 'area is normal!')
    except:
        print('Sorry, temperature data is not available')

    try:
        wind_speed = re.search(r'(?:\d{1,2} MPH|Calm:0)', airport_data).group(0)
        if wind_speed == 'Calm:0':
            print('Wind speed in airport', airport, ' is normal!')
        elif int(wind_speed.split()[0]) < wind_stop:
            print('Wind speed in airport', airport, ' is normal!')
        else:
            print('Attention! Wind speed in airport ', airport, 'is below ', str(wind_stop), '.', sep='')
    except:
        print('Sorry, wind speed data is not available')

    try:
        press = re.search(r'\d{3,4} hPa', airport_data).group(0)
        if int(press.split()[0]) < press_stop:
            print('Attention! Pressure in airport ', airport, ' is below ', str(press_stop), '.', sep='')
        else:
            print('Pressure in airport', airport, 'area is normal!')
    except:
        print('Sorry, pressure data is not available')

def parser_cycle():
    for airport in airports:
        parser(airport, temp_stop, wind_stop, press_stop)
        info = print()
    return render_template('index.html', info=info)