import os
import sys
import argparse
import json
import requests
import datetime

from pwy.translation import TRANSLATIONS_JSON
from pwy.colours import BWHITE, GREEN, RESET, BWHITE
from pwy.ascii import clear_sky, few_clouds, overcast_cloud, rain, \
                    thunderstorm, snow, mist, unknown
from pwy._version import __version__


def get_key():
    """Read the user's OWM API key from the .pwyrc file"""

    home = os.path.expanduser("~")

    if os.name is "posix":
        with open(f"{home}/.config/pwyrc") as f:
            key = f.readline()

        return key
    else:
        with open(f"{home}\.pwyrc") as f:
            key = f.readline()

        return key


def get_weather_data(location, unit, lang):
    """Get weather data from the API and return the necessary data."""

    url = (f"https://api.openweathermap.org/data/2.5/weather?q={location}"
           f"&appid={get_key()}&units={unit}&lang={lang}")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        status = response.status_code
        if status == 401:
            print("Invalid API key.")
        elif status == 404:
            print("Invalid input. See pwy -h for more information.")
        elif status in (429, 443):
            print("API calls per minute exceeded.")

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

    return(
        f"\t{ascii[0]}  {BWHITE}{info['name']}, {info['country']}{RESET}\n"
        f"\t{ascii[1]}  {GREEN}{info['temp']}{RESET} "\
            f"({info['feels_like']}) {units[0]}\n"
        f"\t{ascii[2]}  {info['main']}. {info['description']}\n"
        f"\t{ascii[3]}  {GREEN}{info['pressure']}{RESET}hPa  "\
            f"{GREEN}{info['humidity']}{RESET}%  {BWHITE}{dirs} "\
            f"{GREEN}{info['speed']}{RESET}{units[1]}\n"
        f"\t{ascii[4]}  {GREEN}{time}{RESET}\n"
    )


def configuration(config):
    """Configure OWM API key and save it in the .pwyrc file."""

    home = os.path.expanduser("~")

    if os.name is "posix":
        key_file = open(f"{home}/.config/pwyrc", "w+")
    else:
        key_file = open(f"{home}\.pwyrc", "w+")

    key_file.write(config)
    key_file.close()

    return "Configuration finished."


def main():
    """Get user arguments."""

    parser = argparse.ArgumentParser(
        description = "pwy - A simple weather tool.")

    parser.add_argument("location", nargs = "*", help = "input location")
    parser.add_argument("-c", "--config", dest = "config", metavar = "",
                        help = "configure pwy")
    parser.add_argument("-u", "--unit", dest = "unit", default="metric",
                        metavar = "", help = "input unit")
    parser.add_argument("-l", "--lang", dest = "language", default="en",
                        metavar = "", help = "input language")
    parser.add_argument("-v", "--version", action = "version",
                        version=f"pwy {__version__}")

    args = parser.parse_args()

    location = " ".join(args.location)
    config = args.config
    unit = args.unit
    lang = args.language

    if config is not None:
        print(configuration(config))
    else:
        info = get_weather_data(location, unit, lang)
        print(display_weather_info(info))