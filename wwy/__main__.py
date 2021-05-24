#!/usr/bin/env python3
#
#
# wwy
# Copyright (C) 2021, Clint <github.com/clieg>
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


def get_weather_info(city, unit):
    # Get the data from the API.
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units={unit}"
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
        visibility = data['visibility']
        
        return (name, country, temp, feels_like, main, description, pressure,
            humidity, speed, visibility, unit)
            
    except KeyError:
        print(f"{YELLOW}Invalid input. See wwy -h for more information. {city}")
        sys.exit(1)
    
    
def get_ascii(info):
    # If the conditions are equal to weather, return its designated list
    # containting the ASCII art.
    
    weather = info[5]
    
    if 'Clear Sky' in weather:
        return clear_sky
            
    if ('Few Clouds' in weather or 'Broken Clouds' in weather or
        'Scattered Clouds' in weather):
        return few_clouds
            
    if 'Overcast Cloud' in weather:
        return overcast_cloud
            
    if 'Rain' in weather:
        return rain
            
    if 'Thunderstorm' in weather:
        return thunderstorm
    
    if 'Snow' in weather:
        return snow
            
    if 'Mist' in weather:
        return mist
            
            
def get_units(info):
    # If info[10] is equal to 'metric', return the first index of units.
    # Otherwise, return the second index.
    
    units = ['C', 'F']
    
    if info[10] == 'metric':
        return units[0]
    else:
        return units[1]
        
        
def display_weather_info(info):
    # Invoke the get_ascii() function. Iterate through the list containing the
    # ASCII art and print it.
    # Invoke the get_units() function and print the temperature's measurement.
    
    ascii = get_ascii(info)
    units = get_units(info)
    
    for line in ascii:
        print(f"\t{WHITE}{line}{RESET}")

    
    # Print the weather information.
    print(f"\t{BWHITE}{info[0]}, {info[1]}{RESET}")
    print(f"\t{BWHITE}{info[2]}°{units}{RESET}")
    print(f"\t{WHITE}Feels like {info[3]}°{units}. {info[4]}. {info[5]}{RESET}")
    print(f"\t{WHITE}Pressure: {info[6]}hPa\tHumidity: {info[7]}%\tVisibility: {info[8]}km{RESET}")
            
            
def main():
    # Metric system is used by default.
    # If unit is empty, use metric. Otherwise use Imperial system.
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('city', nargs='+', help='Input city name')
    parser.add_argument('-u', dest='unit', help='Input unit name')
    
    args = parser.parse_args()
    city = ' '.join(args.city)
    unit = args.unit
    
    if unit is None:
        unit = 'metric'
    
    info = get_weather_info(city, unit)
    
    display_weather_info(info)
        
        
if __name__ == '__main__':
    main()
