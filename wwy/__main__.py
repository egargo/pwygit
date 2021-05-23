#!/usr/bin/env python3
#
#
# wwy
# # Copyright (C) 2021, Clint <github.com/clieg>
#
# This is the main file of wwy
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
import sys

from wwy.key import KEY
from wwy.colours import *
from wwy.ascii import *


def get_weather_info(city):
    url     = 'https://api.openweathermap.org/data/2.5/weather?'\
            'q={}&appid={}&units=metric'.format(city, KEY)
    req     = requests.get(url)
    data    = req.json()
    
    try:
        name        = data['name']
        country     = data['sys']['country']
        temp        = data['main']['temp']
        feels_like  = data['main']['feels_like']
        main        = data['weather'][0]['main']
        description = data['weather'][0]['description'].title()
        pressure    = data['main']['pressure']
        humidity    = data['main']['humidity']
        speed       = data['wind']['speed']
        visibility  = data['visibility']
        
        return (name, country, temp, feels_like, main, description, pressure,
            humidity, speed, visibility)
            
    except KeyError:
        print('{}Invalid input {}{}'.format(RED, city, RESET))
        sys.exit()
    
    
def get_ascii(info):
    weather = info[5]
    
    if 'Clear Sky' in weather:
        for i in range(len(clear_sky)):
            print('\t{}{}{}'.format(WHITE, clear_sky[i], RESET))
            
    if 'Few Clouds' in weather:
        for i in range(len(scattered_cloud)):
            print('\t{}{}{}'.format(WHITE, scattered_cloud[i], RESET))
            
    if ('Overcast Clouds' in weather or 'Broken Clouds' in weather or
        'Scattered Clouds' in weather):
        for i in range(len(overcast_cloud)):
            print('\t{}{}{}'.format(WHITE, overcast_cloud[i], RESET))
            
    if 'Rain' in weather:
        for i in range(len(rain)):
            print('\t{}{}{}'.format(WHITE, rain[i], RESET))
            
    if 'Thunderstorm' in weather:
        for i in range(len(thunderstorm)):
            print('\t{}{}{}'.format(WHITE, thunderstorm[i], RESET))
    
    if 'Snow' in weather:
        for i in range(len(snow)):
            print('\t{}{}{}'.format(WHITE, snow[i], RESET))
            
    if 'Mist' in weather:
        for i in range(len(mist)):
            print('\t{}{}{}'.format(WHITE, mist[i], RESET))
            
            
def main():
    # Parse terminal arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-c', '--city', action = 'store', dest = 'city',
        help = 'city; city,country', nargs = '*', type = str, required = True)
    
    args = parser.parse_args()
    city = ' '.join(args.city)
    
    info = get_weather_info(city)
    get_ascii(info)
    
    # Print the weather information.
    print('\t{}{}, {}{}'.format(BWHITE, info[0], info[1], RESET))
    print('\t{}{}°C{}'.format(BWHITE, info[2], RESET))
    print('\t{}Feels like {}°C. {}. {}{}'.format(WHITE, info[3], info[4], info[5], RESET))
    print('\t{}Pressure: {}hPa\tHumidity: {}%\tVisibility: {}km{}'.format(WHITE, info[6], info[7], info[8], RESET))
        
        
if __name__ == '__main__':
    main()