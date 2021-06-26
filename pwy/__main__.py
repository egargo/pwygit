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
import json

from pwy.key import KEY
from pwy.translation import TRANSLATIONS_JSON
from pwy.colours import BWHITE, GREEN, RESET, BWHITE
from pwy.ascii import clear_sky, few_clouds, overcast_cloud, rain, \
                    thunderstorm, snow, mist, unknown


def get_weather_data(location, unit, lang):
    """Get weather data from the API and return the necessary data."""

    url = (f"https://api.openweathermap.org/data/2.5/weather?q={location}"
           f"&appid={KEY}&units={unit}&lang={lang}")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        status = response.status_code
        if status == 401:
            print(f"Invalid API key.")
        elif status == 404:
            print(f"Invalid input. See pwy -h for more information.")
        elif status in (429, 443):
            print(f"API calls per minute exceeded.")

        sys.exit(1)

    data = response.json()

    weather_info = {
        "name": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "main": data["weather"][0]["main"],
        "description": data["weather"][0]["description"].title(),
        "pressure": data["main"]["pressure"],
        "humidity": data["main"]["humidity"],
        "speed": data["wind"]["speed"],
        "deg": data["wind"]["deg"],
        "timezone": data["timezone"],
        "unit": unit,
        "lang": lang
    }

    return weather_info


def get_weather_translation(info):
    """Translate the current weather's description into the user's language."""

    LANGUAGES = json.loads(TRANSLATIONS_JSON)

    if info["lang"] in LANGUAGES["LANGUAGES"]:
        language = LANGUAGES["TRANSLATIONS"][0][info["lang"]]
    else:
        print(f"Invalid input. See pwy -h for more information.")
        sys.exit(1)
    
    return language


def get_ascii(info):
    """Get the weather's ASCII art."""

    weather = info["description"]
    language = get_weather_translation(info)

    if weather == language[0]:
        return clear_sky
    elif weather in (language[1], language[2]):
        return overcast_cloud
    elif weather in (language[3], language[4]):
        return few_clouds
    elif weather in (language[5], language[6], language[7], language[8]):
         return rain
    elif weather == language[9]:
            return thunderstorm
    elif weather == language[10]:
        return snow
    elif weather == language[11]:
            return mist
    else:
        return unknown


def get_units(info):
    """Return the appropriate unit's indecis."""

    units = ["°C", "m/s", "°F", "mph", "K"]

    if info["unit"] == "metric":
        return (units[0], units[1])
    elif info["unit"] == "imperial":
        return (units[2], units[3])
    else:
        return (units[4], units[1])


def get_localtime(info):
    """Convert data['timezone'] to 'Hour:Minute Timezone' format."""

    timezone = datetime.timezone(datetime.timedelta(seconds=info["timezone"]))
    return datetime.datetime.now(tz=timezone).strftime("%H:%M %Z")


def get_wind_direction(info):
    """Convert data['deg'] to cardinal directions."""

    arrows = ["↓", "↙", "←", "↖", "↑", "↗", "→", "↘"]
    direction = int((info["deg"] + 11.25) / 45)
    return arrows[direction % 8]


def display_weather_info(info):
    """Display the weather information."""

    ascii = get_ascii(info)
    units = get_units(info)
    time = get_localtime(info)
    dirs = get_wind_direction(info)

    print(f"\t{ascii[0]}  {BWHITE}{info['name']}, {info['country']}{RESET}")
    print(f"\t{ascii[1]}  {GREEN}{info['temp']}{RESET}"
          f" ({info['feels_like']}) {units[0]}")
    print(f"\t{ascii[2]}  {info['main']}. {info['description']}")
    print(f"\t{ascii[3]}  {GREEN}{info['pressure']}{RESET}hPa"
          f"  {GREEN}{info['humidity']}{RESET}%"
          f"  {BWHITE}{dirs} {GREEN}{info['speed']}{RESET}{units[1]}")
    print(f"\t{ascii[4]}  {GREEN}{time}{RESET}")

    sys.exit()


def main():
    """Get user arguments."""

    parser = argparse.ArgumentParser(
        description = "pwy - A simple weather tool.")

    parser.add_argument("location", nargs = "+", help = "Input location")
    parser.add_argument("--unit", dest = "unit", metavar = "",
                        help = "Input unit")
    parser.add_argument("--lang", dest = "language", metavar = "",
                        help = "Input language")

    args = parser.parse_args()

    location = " ".join(args.location)
    unit = args.unit
    lang = args.language
 
    if unit is None:
        unit = "metric"
    if lang is None:
        lang = "en"

    info = get_weather_data(location, unit, lang)
    display_weather_info(info)


if __name__ == "__main__":
    main()