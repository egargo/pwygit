<div align="center">
    <h1>pwy</h1>
    <p>A simple weather tool.</p>
    <img src="https://raw.githubusercontent.com/notclint/notclint.github.io/master/images/pwy.png"><br>
    <a href="https://pypi.org/project/pwy"><img src="https://img.shields.io/pypi/v/pwy"></a>
    <a href="https://openweathermap.org/api"><img src="https://img.shields.io/badge/openweathermap-api-blue"></a>
    <a href="https://github.com/notclint/pwy/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-GPL&#8208;3.0-blue"></a>
</div>

## Table of Contents
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Usage](#usage)
* [Update](#update)
* [Changelog](#changelog)
* [Credits](#credits)
* [License](#license)

## Dependencies
* `python 3.6+`
* `requests`


## Installation
### Pip install
#### Unix-like
```sh
pip3 install pwy
```
#### Windows
```sh
pip install pwy
```
### Manual/Git install
#### Unix-like
```sh
# If you have Git installed, git clone the repository.
git clone https://github.com/notclint/pwy
cd pwy

# Add your OpenWeatherMap API key in the pwy/key.py file.
vim pwy/key.py

# Install pwy.
pip3 install .
```


## Usage
### Unix-like
```sh
# To display weather in your current city.
pwy tokyo

# You can also specify what country you are in by.
pwy tokyo,jp

# To display weather with specific unit of measurement. By default the unit is Metric system.
pwy tokyo --unit imperial

# To display weather with specific language.
pwy tokyo --lang ja
```
### Windows
```sh
pwy tokyo,jp | Write-Host
```


## Update
### Unix-like
```sh
pip3 install --upgrade pwy
```
### Windows
```sh
pip install --upgrade pwy
```


## Changelog
View [Changelog](https://github.com/notclint/pwy/blob/master/CHANGELOG.md).


## Credits
* [pwy Contributors](https://github.com/notclint/pwy/graphs/contributors)
* [OpenWeatherMap](https://openweathermap.org/current) - API
* [wego](https://github.com/schachmat/wego) - ASCII art


## License
This program is provided under the [GPL-3.0 License](https://github.com/notclint/pwy/blob/master/LICENSE).