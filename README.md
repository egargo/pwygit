<div align="center">
    <h1>pwy</h1>
    <p>A simple weather tool.</p>
    <img src="https://raw.githubusercontent.com/noqqlint/windybroth.github.io/master/images/pwy.png"><br>
    <a href="https://pypi.org/project/pwy"><img src="https://img.shields.io/pypi/v/pwy"></a>
    <a href="https://openweathermap.org/api"><img src="https://img.shields.io/badge/openweathermap-api-blue"></a>
    <a href="#"><img src="https://static.pepy.tech/personalized-badge/pwy?period=total&units=none&left_color=grey&right_color=blue&left_text=downloads"></a>
    <a href="https://github.com/noqqlint/pwy/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-GPL&#8208;3.0-blue"></a>
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


## Dependencies
* OpenWeatherMap API key
* Python 3.8
    * requests


## Installation
### Pip install
#### Unix-like | Windows (Cygwin/WSL)
```sh
pip3 install pwy
```

### Manual/Git install
#### Unix-like | Windows (Cygwin/WSL)
```sh
# If you have Git installed, git clone the repository.
git clone https://github.com/noqqlint/pwy

# Go to pwy directory.
cd pwy

# Install pwy.
pip3 install .
```


## Configuration
### Unix-like | Windows (Cygwin/WSL)
Before you can use pwy, you need to configure your OWM API key first. After you're through, the `.pwyrc` config file, containing your OWM API key will be generated in your home directory. Get your OWM key by [signing up](https://home.openweathermap.org/users/sign_up).
```sh
# Configure pwy with your OWM API key.
pwy --config XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```


## Usage
### Unix-like | Windows (Cygwin/WSL)
```sh
# To display weather in your current city.
pwy tokyo

# You can also specify what country you are in by.
pwy tokyo,jp

# To display weather with specific unit of measurement. By default the unit is Metric system.
pwy tokyo --unit imperial

# To display weather with specific language.
pwy tokyo --lang ja

# To display help information.
pwy --help
```


## Update
### Unix-like | Windows (Cygwin/WSL)
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