<div align="center">
    <h1>pwy</h1>
    <p>A simple weather tool.</p>
    <img src="https://raw.githubusercontent.com/clieg/clieg.github.io/master/images/pwy.png"><br>
    <a href="https://pypi.org/project/pwy"><img src="https://img.shields.io/pypi/v/pwy"></a>
    <a href="https://openweathermap.org/api"><img src="https://img.shields.io/badge/openweathermap-api-blue"></a>
    <a href="https://github.com/clieg/pwy/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-GPL&#8208;3.0-blue">
</div>

# Table of Contents
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Usage](#usage)
* [Update](#update)
* [Credits](#credits)
* [License](#license)

## Dependencies
* `python` - 3.5 or greater
* `requests` - for fetching HTTP requests


## Installation
Unix-like
```bash
pip3 install pwy
```

Windows
```bash
pip install pwy
```

## Usage
To display weather in your current city
```bash
pwy tokyo
```

You can also specify what country you are in by
```bash
pwy tokyo,jp
```

To display weather with specific unit of measurement. By default the unit is Metric system.
```bash
pwy tokyo --unit imperial
```

To display weather with specific language.
```bash
pwy tokyo --lang ja
```


## Update
Unix-like
```bash
pip3 install --upgrade pwy
```

Windows
```bash
pip install --upgrade pwy
```


## Credits
* [pwy Contributors](https://github.com/clieg/pwy/graphs/contributors)
* [OpenWeatherMap](https://openweathermap.org/current) - API
* [wego](https://github.com/schachmat/wego) - ASCII art

## License
Made by [Clint E](https://github.com/clieg). This program is provided under the [GPL-3.0 License](https://github.com/clieg/pwy/blob/master/LICENSE).