<div align="center">
    <h1>pwy</h1>
    <p>A simple weather tool.</p>
    <img src="https://raw.githubusercontent.com/clieg/clieg.github.io/master/images/pwy.png"><br>
    <a href="https://pypi.org/project/pwy"><img src="https://img.shields.io/pypi/v/pwy"></a>
    <a href="https://pypi.org/project/pwy"><img src="https://img.shields.io/pypi/dm/pwy"></a>
    <a href="https://openweathermap.org/api"><img src="https://img.shields.io/badge/openweathermap-api-blue"></a>
    <a href="https://github.com/clieg/pwy/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-GPL&#8208;3.0-blue"></a>
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
### PyPi
#### Unix-like
```sh
pip3 install pwy
```
#### Windows
```sh
pip install pwy
```


## Usage
#### Unix-like
To display weather in your current city
```sh
pwy tokyo
```
You can also specify what country you are in by
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
#### Windows
```sh
pwy tokyo,jp | Write-Host
```


## Update
#### Unix-like
```sh
pip3 install --upgrade pwy
```
#### Windows
```sh
pip install --upgrade pwy
```


## Changelog
View [Changelog](https://github.com/clieg/pwy/blob/master/CHANGELOG.md).


## Credits
* [pwy Contributors](https://github.com/clieg/pwy/graphs/contributors)
* [OpenWeatherMap](https://openweathermap.org/current) - API
* [wego](https://github.com/schachmat/wego) - ASCII art


## License
This program is provided under the [GPL-3.0 License](https://github.com/clieg/pwy/blob/master/LICENSE).