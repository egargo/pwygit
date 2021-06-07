#!/usr/bin/env python3
#
#
# pwy
# Copyright (C) 2021, Clint <https://github.com/clieg>
#
# This is the main file of pwy
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
from datetime import timedelta

from pwy.key import KEY
from pwy.colours import *
from pwy.ascii import *
from pwy.translation import lang_list, TRANSLATION


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
        dt = data['timezone']
        tz = data['dt']
        
        return (name, country, temp, feels_like, main, description, pressure,
            humidity, speed, dt, tz, unit, lang)
            
    except:
        req = str(req)
        
        if '401' in req:
            print(f'{req}: Invalid API key.')
            
        if '404' in req:
            print(f'{req}: Invalid input. '
                f'See pwy -h for more information.')
            
        if '429' in req:
            print(f'{req}: API calls per minute exceeded.')
            
        if '443' in req:
            print(f'{req}: Max retries exceeded with url.')
    
    
def get_ascii(info):
    # Find the language. If the language is present, get the key of TRANSLATION
    # dictionary that matches the language and return the designated list
    # containing the weather ASCII art of the conditions are met.
    
    weather = info[5]
    lang = info[12]
    
    for index in range(len(lang_list)):
        if lang == lang_list[index]:
            language = TRANSLATION.get(lang)
            
            if weather == language[0]:
                return clear_sky
            
            if (weather == language[1] or weather == language[2]):
                return overcast_cloud
                
            if (weather == language[3] or weather == language[4]):
                return few_clouds
                
            if (weather == language[5] or weather == language[6]
                or weather == language[7]):
                return rain
                
            if weather == language[8]:
                return thunderstorm
                
            if weather == language[9]:
                return snow
                
            if weather == language[10]:
                return mist
                
            else:
                return unknown
            
            
def get_units(info):
    # If info[9] is equal to 'metric', return the first first and second index.
    # Otherwise, return the second and third index.
    
    units = ['C', 'km/h', 'F', 'mph']
    
    if info[11] == 'metric':
        return (units[0], units[1])
    else:
        return (units[2], units[3])
        
        
def get_localtime(info):
    # Get the local time and timezone.
    
    localtime = datetime.timezone(datetime.timedelta(seconds = (info[9])))
    return datetime.datetime.now(tz = localtime).strftime('%H:%M %Z')
    
    
def display_weather_info(info):
    # Invoke the get_ascii() function. Iterate through the list containing the
    # ASCII art and print it.
    # Invoke the get_units() function and print the temperature's measurement.
    # Invoke the get_localtime function and print the local time.
    
    ascii = get_ascii(info)
    units = get_units(info)
    local_time = get_localtime(info)
    
    # Print the weather information.
    print(f'\t{ascii[0]}  {BWHITE}{info[0]}, {info[1]}{RESET}')
    print(f'\t{ascii[1]}  Temperature: {GREEN}{info[2]}°{units[0]}{RESET}'
          f' ({info[3]}°{units[0]})')
    print(f'\t{ascii[2]}  {info[4]}. {info[5]}')
    print(f'\t{ascii[3]}  Pressure: {GREEN}{info[6]}{RESET}hPa'
          f'  Humidity: {GREEN}{info[7]}{RESET}%'
          f'  Wind: {GREEN}{info[8]}{RESET}{units[1]}')
    print(f'\t{ascii[4]}  Time: {local_time}')
            
            
def main():
    # Get arguments.
    # Metric system is used by default.
    # If unit is empty, use Metric system. Otherwise use Imperial system.
    
    parser = argparse.ArgumentParser(
        description = 'pwy - A simple weather tool.')
    
    parser.add_argument('city', nargs='+', help='Input city name')
    parser.add_argument('--unit', dest = 'unit', help='Input unit name')
    parser.add_argument('--lang', dest = 'language', help='Input language')
    
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