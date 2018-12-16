# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from requests import *
from metar import Metar

@app.route('/')

@app.route('/index')
def check_for_trig(station):
    source = 'http://tgftp.nws.noaa.gov/data/observations/metar/stations/'
    #stations = ['ENSO', 'KBVX', 'RJDT', 'FSIA', 'YCNM', 'EGOW', 'CWBK', 'UAOO', 'KMBY', 'KOPN', 'PAMB', 'CXKA', 'K21D',
    #           'CYLC', 'EKAH', 'LTAR', 'RJCT', 'SKVV', 'KO69', 'YLEC', 'ETNN', 'KSPB', 'LFQQ', 'KMWL', 'EFET', 'CWQO',
    #           'KLNN', 'K2D5', 'YBRM', 'K9D7']
    stat = 'ENSO'
    formatik = '.TXT'
    # triggers
    temp_stop = -20
    wind_stop = 5
    ##is lower
    press_stop = 995
    kt = 1.1507794480136

    target_url = source + stat + formatik
    response = get(target_url)
    code = response.text[17:-1]
    obs = Metar.Metar(code)

    #try:
    #    obs = Metar.Metar(code)
    #except:
    #    print('Airport data is incorrect')
    #pass

    try:
        if obs.code() is not None:
            station_name = obs.code()
        else:
            station_name = 'No station name'
    except:
        station_name = 'Some problem with parsing data about name'

    try:
        if obs.temp.value() <= temp_stop:
            temperature = 'Look out! Temperature in ' + station + ' is lower than ' + str(temp_stop) + ' C !'
        else:
            temperature = 'Temperature in ' + station + ' is OK!'
    except:
        temperature = 'Some problem with parsing temperature data'

    try:
        if obs.wind_speed.value() * kt >= wind_stop:
            wind = 'Wind in ' + station + ' is more than ' + str(wind_stop) + ' mph !'
        else:
            wind = 'Wind in ' + station + ' is OK!'
    except:
        wind = 'Some problem with parsing wind data'

    try:
        if obs.press is None:
            press = obs.press_sea_level.value()
        elif obs.press.value() < 100:
            press = obs.press_sea_level.value()
        else:
            press = obs.press.value()
    except:
        press = None
    try:
        if press < press_stop and press is not None:
            pressure = 'Pressure in ' + station + ' is lower than ' + str(press_stop) + ' hPa !'
        else:
            pressure = 'Pressure in ' + station + ' is OK!'
    except:
        pressure = 'Some problem with parsing pressure data'

    #i = 0
    #for st in stations:
    #    print('№', str(i), end=' ')
    #    print(st, ':', sep='')
    #    check_for_trig(st)
    #    print()
    #    i += 1
    return render_template('index.html', station_name = station_name, temperature = temperature, wind=wind, pressure = pressure)