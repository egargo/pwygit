<div align="center">
    <h1>pwy</h1>
    <p>A simple weather tool.</p>
    <img src="https://raw.githubusercontent.com/noqqlint/noqqlint.github.io/master/images/pwy.png"><br>
    <a href="https://pypi.org/project/pwy"><img src="https://img.shields.io/pypi/v/pwy"></a>
    <a href="https://openweathermap.org/api"><img src="https://img.shields.io/badge/openweathermap-api-blue"></a>
    <a href="#"><img src="https://static.pepy.tech/personalized-badge/pwy?period=total&units=none&left_color=grey&right_color=blue&left_text=downloads"></a>
    <a href="https://github.com/noqqlint/pwy/blob/master/LICENSE"><img src="https://img.shields.io/pypi/l/pwy?color=blue"></a>
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
    * Weather and weahter description.
    * Wind pressure, humidity, wind direction, and wind speed.
    * Time and timezone of the location.


## Dependencies
* OpenWeatherMap API key
* Python 3.8
    * requests
	* rich


## Installation
### Pip install
#### Unix-like | Windows
```sh
pip3 install pwy
```

### Manual/Git install
#### Unix-like | Windows

Download the latest pwy package [here](https://github.com/noqqlint/pwy/releases/latest) and uncompress it.
Go to pwy directory.
```sh
cd pwy
```
Install pwy.
```
pip3 install .
```


## Configuration
### Unix-like | Windows
Before you can use pwy, you need to configure your OWM API key first. After you're through, the `pwyrc` (`~/.config/pwyrc` for Unix-like and `.pwyrc` for Windows) config file, containing your OWM API key will be generated. Get your OWM key by [signing up](https://home.openweathermap.org/users/sign_up).

* After creating your OWM API key you have to wait a couple of minutes for your API key to activate.
* This only applies to Unix-like users: If you just install pwy version 1.4.3, please delete the `.pwyrc` in your home director.
Configure pwy with your OWM API key.
```sh
pwy --config XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```


## Usage
### Unix-like | Windows
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


## Update
### Unix-like | Windows
```sh
pip3 install --upgrade pwy
```


## Changelog
View [Changelog](https://github.com/noqqlint/pwy/blob/master/CHANGELOG.md).


## Credits
* [pwy Contributors](https://github.com/noqqlint/pwy/graphs/contributors)
* [OpenWeatherMap](https://openweathermap.org/current) - API
* [wego](https://github.com/schachmat/wego) - ASCII art


## License
This program is provided under the [GPL-3.0 License](https://github.com/noqqlint/pwy/blob/master/LICENSE).
