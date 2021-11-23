import os
import sys
import argparse
import json
import requests
import datetime
from rich import print

from pwy.translation import TRANSLATIONS_JSON
from pwy.ascii import (
    clear_sky,
    few_clouds,
    overcast_cloud,
    rain,
    thunderstorm,
    snow,
    mist,
    unknown,
)
from pwy._version import __version__


def get_config_data():
    """Read the user's OWM API key from the pwy.json file"""

    config = {}

    home = os.path.expanduser("~")

    if os.name == "posix":
        with open(f"{home}/.config/pwy.json") as pwy_json:
            data = json.load(pwy_json)
            for key, value in data.items():
                config[key] = value
        return config
    else:
        with open(f"{home}\pwy.json") as pwy_json:
            data = json.load(pwy_jsoon)
            for key, value in data.items():
                config[key] = value
        return config


def get_weather_data(location, unit, lang):
    """Get weather data from the API and return the necessary data."""

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={location}"
        f"&appid={get_config_data()['api_key']}&units={unit}&lang={lang}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        status = response.status_code
        if status == 401:
            print("[orange1]Invalid API key.[/]")
        elif status == 404:
            print("[orange1]Invalid input. See pwy -h for more information.[/]")
        elif status in (429, 443):
            print("[orange1]API calls per minute exceeded.[/]")

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
        "lang": lang,
    }

    return weather_info


def get_weather_translation(info):
    """Translate the current weather's description into the user's language."""

    LANGUAGES = json.loads(TRANSLATIONS_JSON)

    if info["lang"] in LANGUAGES["LANGUAGES"]:
        language = LANGUAGES["TRANSLATIONS"][0][info["lang"]]
    else:
        print("[orange1]Invalid input. See pwy -h for more information.[/]")

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

    return (
        f"\t{ascii[0]}  [b white]{info['name']}, {info['country']}[/]\n"
        f"\t{ascii[1]}  [green]{info['temp']}[/] "
        f"({info['feels_like']}) {units[0]}\n"
        f"\t{ascii[2]}  [b white]{info['main']}[/]. {info['description']}\n"
        f"\t{ascii[3]}  [b green]{info['pressure']}[/]hPa  "
        f"[b green]{info['humidity']}[/]%  [b white]{dirs}[/] "
        f"[b green]{info['speed']}[/]{units[1]}\n"
        f"\t{ascii[4]}  {time}\n"
    )


def configuration():
    """Configure OWM API key and save it in the pwy.json file."""

    config = {}

    config["api_key"] = input("OWM API key            : ")
    config["location"] = input("Location               : ")
    config["unit"] = input("Unit (metric/imperial) : ") or "metric"
    config["lang"] = input("Language               : ") or "en"

    home = os.path.expanduser("~")

    if os.name == "posix":
        with open(f"{home}/.config/pwy.json", "w+") as pwy_json:
            json.dump(config, pwy_json, indent=4)
    else:
        with open(f"{home}\pwy.json", "w+") as pwy_json:
            json.dump(config, pwy_json, indent=4)

    return "[green]Configuration finished.[/]"


def main():
    """Get user arguments."""

    try:
        parser = argparse.ArgumentParser(
            description="pwy - A simple weather information tool"
        )

        data = get_config_data()

        parser.add_argument(
            "location",
            nargs="*",
            default=f"{data['location']}",
            help="input location",
        )
        parser.add_argument("-c", "--config", action="store_true", help="configure pwy")
        parser.add_argument(
            "-u",
            "--unit",
            dest="unit",
            default=f"{data['unit']}",
            metavar="",
            help="input unit",
        )
        parser.add_argument(
            "-l",
            "--lang",
            dest="language",
            default=f"{data['lang']}",
            metavar="",
            help="input language",
        )
        parser.add_argument(
            "-v", "--version", action="version", version=f"pwy {__version__}"
        )

        args = parser.parse_args()
        location = " ".join(args.location) if len(sys.argv) > 1 else args.location
        config = args.config
        unit = args.unit
        lang = args.language

        if config:
            print(configuration())
        else:
            info = get_weather_data(location, unit, lang)
            print(display_weather_info(info))
    except FileNotFoundError:
        print("[orange1]pwy.json does not exist.[/]\n")
        print(configuration())
