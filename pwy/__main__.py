#!/usr/bin/env python3
#
# pwy
# Copyright (C) 2021, Clint <https://github.com/clieg>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import requests
import argparse
import datetime
import sys

from pwy.key import KEY
from pwy.colours import BWHITE, GREEN, RESET
from pwy.ascii import *
from pwy.translation import LANGUAGES, TRANSLATIONS


def get_weather_info(city, unit, lang):
    # Get the data from the API.
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units={unit}&lang={lang}'
    req = requests.get(url)
    data = req.json()
    
    try:
        name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        main = data['weather'][0]['main']
        description = data['weather'][0]['description'].title()
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        speed = data['wind']['speed']
        timezone = data['timezone']
        
        return (name, country, temp, feels_like, main, description, pressure,
            humidity, speed, timezone, unit, lang)
            
    except:
        req = str(req)
        
        if '401' in req:
            print(f'Invalid API key.')
        elif '404' in req:
            print(f'Invalid input. See pwy -h for more information.')
        elif '429' in req or '443' in req:
            print(f'API calls per minute exceeded.')

        sys.exit(1)


def get_ascii(info):
    # Find the language. If the language is present, get the key of TRANSLATION
    # dictionary that matches the language and return the designated list
    # containing the weather ASCII art of the conditions are met.
    
    weather = info[5]
    lang = info[11]
    
    for index in range(len(LANGUAGES)):
        if lang == LANGUAGES[index]:
            language = TRANSLATIONS.get(lang)
            
            if weather == language[0]:
                return clear_sky
            
            elif (weather == language[1] or weather == language[2]):
                return overcast_cloud
                
            elif (weather == language[3] or weather == language[4]):
                return few_clouds
                
            elif (weather == language[5] or weather == language[6]
                or weather == language[7]):
                return rain
                
            elif weather == language[8]:
                return thunderstorm
                
            elif weather == language[9]:
                return snow
                
            elif weather == language[10]:
                return mist
                
            else:
                return unknown


def get_units(info):
    # If info[9] is equal to 'metric', return the first first and second index.
    # Otherwise, return the second and third index.

    units = ['°C', 'm/s', '°F', 'mph', 'K']
    
    if info[10] == 'metric':
        return (units[0], units[1])
    elif info[10] == 'imperial':
        return (units[2], units[3])
    else:
        return (units[4], units[1])


def get_localtime(info):
    # Get the local time and timezone.

    timezone = datetime.timezone(datetime.timedelta(seconds = (info[9])))
    return datetime.datetime.now(tz = timezone).strftime('%H:%M %Z')


def display_weather_info(info):
    # Invoke the get_ascii() function and print it by index.
    # Invoke the get_units() function and print the temperature's measurement.
    # Invoke the get_localtime function and print the local time.

    ascii = get_ascii(info)
    units = get_units(info)
    time = get_localtime(info)
    
    # Print the weather information.
    print(f'\t{ascii[0]}  {BWHITE}{info[0]}, {info[1]}{RESET}')
    print(f'\t{ascii[1]}  Temperature: {GREEN}{info[2]}{RESET}'
          f' ({info[3]}) {units[0]}')
    print(f'\t{ascii[2]}  {info[4]}. {info[5]}')
    print(f'\t{ascii[3]}  Pressure: {GREEN}{info[6]}{RESET}hPa'
          f'  Humidity: {GREEN}{info[7]}{RESET}%'
          f'  Wind: {GREEN}{info[8]}{RESET}{units[1]}')
    print(f'\t{ascii[4]}  Time: {GREEN}{time}{RESET}')


def main():
    # Get arguments.
    # Metric system is used by default. If unit is empty, use Metric system.
    # Otherwise use Imperial system.
    
    parser = argparse.ArgumentParser(
        description = 'pwy - A simple weather tool.')
    
    parser.add_argument('city', nargs='+', help='Input city name')
    parser.add_argument('--unit', dest = 'unit', metavar='', help='Input unit name')
    parser.add_argument('--lang', dest = 'language', metavar='', help='Input language')
    
    args = parser.parse_args()
    
    city = ' '.join(args.city)
    unit = args.unit
    lang = args.language
    
    if unit is None:
        unit = 'metric'
    if lang is None:
        lang = 'en'
    
    info = get_weather_info(city, unit, lang)
    display_weather_info(info)


if __name__ == '__main__':
    main()