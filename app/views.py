# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from requests import *
import re

@app.route('/')

@app.route('/index')
def parser():
    airports = ['ENSO', 'KBVX', 'RJDT', 'FSIA', 'YCNM', 'EGOW', 'CWBK', 'UAOO', 'KMBY', 'KOPN', 'PAMB', 'CXKA', 'K21D',
                'CYLC', 'EKAH', 'LTAR', 'RJCT', 'SKVV', 'KO69', 'YLEC', 'ETNN', 'KSPB', 'LFQQ', 'KMWL', 'EFET', 'CWQO',
                'KLNN', 'K2D5', 'YBRM', 'K9D7']

    source = 'http://tgftp.nws.noaa.gov/data/observations/metar/decoded/'
    temp_stop = -20
    wind_stop = 5
    press_stop = 995

    info_all = []

    for airport in airports:
        target_url = source + airport + '.TXT'
        airport_data = get(target_url).text.strip()

        info = 'Airport {} : '.format(airport)
        try:
            temp = re.search(r'[-]?(?:\d{1,2}|\d{1,2}\.\d) C', airport_data).group(0)
            info += 'Temperature is {}. '.format(temp)
            if float(temp.split()[0]) < temp_stop:
                temperature = 'Attention! Temperature in airport {} is below {} C. '.format(airport, temp_stop)
            else:
                temperature = 'Temperature in airport {} is normal! '.format(airport)
        except:
            temperature = 'Sorry, temperature data is not available '
        info += temperature
        try:
            wind_speed = re.search(r'(?:\d{1,2} MPH|Calm:0)', airport_data).group(0)
            info += 'Wind speed is {}. '.format(wind_speed)
            if wind_speed == 'Calm:0':
                wind = 'Wind speed in airport {} is normal! '.format(airport)
            elif int(wind_speed.split()[0]) < wind_stop:
                wind = 'Wind speed in airport is normal! '.format(airport)
            else:
                wind = 'Attention! Wind speed in airport {} is below {} MPH. '.format(airport, wind_stop)
        except:
            wind = 'Sorry, wind speed data is not available '

        info += wind

        try:
            press = re.search(r'\d{3,4} hPa', airport_data).group(0)
            info += 'Pressure is {}. '. format(press)
            if int(press.split()[0]) < press_stop:
                pressure = 'Attention! Pressure in airport {} is below {} hPa. '.format(airport,press_stop)
            else:
                pressure = 'Pressure in airport {} is normal! '.format(airport)
        except:
            pressure = 'Sorry, pressure data is not available '
        info += pressure

        info_all += [{'airport_info': {'airport': airport}, 'report': info}]

    return render_template('index.html', info_all=info_all)
