<div align="center">
    <h1>pwy</h1>
    <p>A simple weather information tool.</p>
    <img src="pwy.png"><br>
    <a href="https://pypi.org/project/pwy"><img src="https://img.shields.io/pypi/v/pwy"></a>
    <a href="https://openweathermap.org/api"><img src="https://img.shields.io/badge/openweathermap-api-blue"></a>
    <a href="#"><img src="https://static.pepy.tech/personalized-badge/pwy?period=total&units=none&left_color=grey&right_color=blue&left_text=downloads"></a>
    <a href="https://github.com/cliegargo/pwy/blob/master/LICENSE"><img src="https://img.shields.io/pypi/l/pwy?color=blue"></a>
</div>


## Table of Contents
* [Features](#features)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Usage](#usage)
* [Update](#update)
* [Changelog](#changelog)
* [Credits](#credits)
* [License](#license)


## Features
* ASCII art
* Display weather information
    * The name of the location.
    * Temperature (and what the temperature feels like).
    * Weather and weather description.
    * Wind pressure, humidity, wind direction, and wind speed.
    * Time and timezone of the location.


## Dependencies
* OpenWeatherMap API key
* Python 3.8
    * requests
	* rich
* Internet connection


## Installation
### Pip install
#### Unix-like | Windows
```sh
pip3 install pwy
```

### Manual/Git install
#### Unix-like | Windows

Download the latest pwy package [here](https://github.com/cliegargo/pwy/releases/latest) and uncompress it.
Go to pwy directory.
```sh
cd pwy
```
Install pwy.
```sh
pip3 install .
```


## Configuration
### Unix-like | Windows
Before you can use pwy, you need to configure pwy. Run the command below and fill the required files, these fields are for the OWM API key, location, unit, and language.
```sh
pwy
```
After you're through, the `pwy.json` (`~/.config/pwy.json` for Unix-like and `pwy.json` for Windows) config file, containing your OWM API key, location, unit, and language, will be generated.

Get your OWM key by [signing up](https://home.openweathermap.org/users/sign_up).

If you want to edit your pwy configuration.
```sh
pwy --config
```


## Usage
### Unix-like | Windows
To display weather in your current city (from pwy.json).
```sh
pwy
```

To display weather in your current city.
```sh
pwy tokyo
```

You can also specify what country you are in by.
```sh
pwy tokyo,jp
```

To display weather with specific unit of measurement. By default the unit is Metric system.
```sh
pwy tokyo --unit imperial
```
To display weather with specific language.
```sh
pwy tokyo --lang ja
```
To display help information.
```sh
pwy --help
```

## Availabe options
```sh
usage: pwy [-h] [-c] [-u] [-l] [-v] [location [location ...]]

pwy - A simple weather information tool

positional arguments:
  location       input location

optional arguments:
  -h, --help     show this help message and exit
  -c, --config   configure pwy
  -u , --unit    input unit
  -l , --lang    input language
  -v, --version  show program's version number and exit
```


## Update
### Unix-like | Windows
```sh
pip3 install --upgrade pwy
```


## Changelog
View [Changelog](https://github.com/cliegargo/pwy/blob/master/CHANGELOG.md).


## Credits
* [pwy Contributors](https://github.com/cliegargo/pwy/graphs/contributors)
* [OpenWeatherMap](https://openweathermap.org/current) - API
* [wego](https://github.com/schachmat/wego) - ASCII art


## License
This program is provided under the [GPL-3.0 License](https://github.com/cliegargo/pwy/blob/master/LICENSE).
