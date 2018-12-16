# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from requests import *
#from metar import Metar
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
    for airport in airports:
        target_url = source + airport + '.TXT'
        airport_data = get(target_url).text.strip()

        station_name = 'Airport ', airport, ':'
        try:
            temp = re.search(r'[-]?(?:\d{1,2}|\d{1,2}\.\d) C', airport_data).group(0)
            if float(temp.split()[0]) < temp_stop:
                temperature = 'Attention! Temperature in airport ', airport, ' is below ', str(temp_stop), '.'
            else:
                temperature = 'Temperature in airport', airport, 'area is normal!'
        except:
            temperature = 'Sorry, temperature data is not available'

        try:
            wind_speed = re.search(r'(?:\d{1,2} MPH|Calm:0)', airport_data).group(0)
            if wind_speed == 'Calm:0':
                wind = 'Wind speed in airport', airport, ' is normal!'
            elif int(wind_speed.split()[0]) < wind_stop:
                wind = 'Wind speed in airport', airport, ' is normal!'
            else:
                wind = 'Attention! Wind speed in airport ', airport, 'is below ', str(wind_stop), '.'
        except:
            wind = 'Sorry, wind speed data is not available'

        try:
            press = re.search(r'\d{3,4} hPa', airport_data).group(0)
            if int(press.split()[0]) < press_stop:
                pressure = 'Attention! Pressure in airport ', airport, ' is below ', str(press_stop), '.'
            else:
                pressure = 'Pressure in airport', airport, ' is normal!'
        except:
            pressure = 'Sorry, pressure data is not available'
        return render_template('index.html', station_name = station_name, temp =temp, temperature = temperature, wind_speed = wind_speed, wind = wind, press =press, pressure =pressure)

#def parser_cycle():
#    for airport in airports:
#        parser(airport, temp_stop, wind_stop, press_stop)
#    return render_template('index.html', info=info)