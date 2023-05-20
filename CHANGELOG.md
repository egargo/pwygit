# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.1.2] - 2022.12.25

- Changed license from GPLv3 to [MIT](./LICENSE).
  - Added MIT License notice to source code files
- Added requirements.txt
- Removed unused codes
- Implemented comprehensions
- Formatted with autopep8
- Added .vscode settings

## 1.4.7 - 2021.12.05 (Patch)

- [Windows] Fixed typo in pwy/cli.py #13 (@patevs).

## 1.4.6 - 2021.12.01

- Fixed KeyError in cli.py
- Added default value when configuring unit and language for `pwy.json`.

## [1.4.5] - 2021.11.09

- Replaced `pwyrc` with `pwy.json`.
  - pwy.json
    - Set OWM API key.
    - Set default location.
    - Set default unit.
    - Set default language.
- Ability to display weather using the `pwy` command.
  - pwy reads the values set in the pwy.json file.
  - If there is/are arguments, `pwy` will satisfy the arguments.
- Minor code cleanup.

## [1.4.4] - 2021.09.30

- Implemented rich.
- Replaced colours.py with rich library.
- Removed colours.py.
- Formatted using black module.
- Minor code cleanup

## [1.4.3] - 2021.09.26

- Added default value to the arguments and removed the unnecessary if else.
- Removed the unnecessary f-strings
- Added `sys.exit(1)`.
- Moved `.pwyrc` to `~/.config/pwyrc` (in Unix-like OS).
- Minor code refactor.

## [1.4.2] - 2021.09.17

- Moved `__main__.py` to `cli.py`.
- Added `_version.py`.
- Added `--version` argument.
- Remove `key.py`.
- Added `--config` argument to setup pwy.
- API key is now stored in `.pwyrc`.

## 1.4.1 - 2021.08.27 [YANKED]

- Changed `key.py` to `key.json`
- Removed the `main` function and its contents to `if __name__ == "__main__`.

## [1.4.0] - 2021.06.26

- Separated get_ascii() and get_weather_translation().
- Removed the output labels.
- Added main.py
- Added zip and tar.gz archives for manual installation.

## 1.3.1 - 2021.06.22

- Refactored `__main__.py` to process JSON.
- Refactored `translation.py` for easier access and readability.
- Added `run_pwy.py` for manual installation.
- Updated the API key and removed the API key in the `key.py` file. PyPi package can still be used without any problems.
- Added a space before between the wind direction and wind speed.
- Removed unused variable.

## 1.3.0 - 2021.06.19

- Added wind direction.
- Wildcard imports removed.
- Merged pull request #7 from @ChaseParate.
- Known issues:
  - Incomplete translation for Heavy Intensity Rain
  - Missing weather translations for Heavy Rain, Thunderstorm, and Snow.
  - No translations for Arabic, Persian, and Hebrews languages.

## 1.2.1 - 2021.06.12

- Patch
  - Added `requests` on setup.py.

## 1.2.0 - 2021.06.12

- Added `standard` unit (Kelvin).
- Added text colour on the current time.
- Minor code refactor:
  - Changed pwy/translation.py: `lang_list` to `LANGUAGES`.
  - Removed wildcard import for `colours`
- Added `Mist` translation.

## 1.1.1 - 2021.06.08

- Fixed the local time and time zone.
- Minor ASCII art fix to match the new UI.

## 1.1.0 - 2021.06.07

- Added Moderate Rain translation.
- Added local time (24 hour format) and time zone.

## [1.0.0] - 2021.06.03

- Name change from `wwy` to `pwy`.
- Revamped UI.
- `--unit` argument for the units (metric, imperial).
- `--lang` argument for the languages.
- Added translations.

- Known issues
  - Missing weather translations for Moderate Rain, Heavy Rain, Thunderstorm, Snow, and Snow.
  - No translations for Arabic, Persian, and Hebrews languages.

## 0.1.4

- Minor typo fix.

## 0.1.3

- Changed .format() to f-string.
- Added wind speed information.

## 0.1.2

- Fixed the incorrect ASCII art.

## 0.1.1

- Minor fixes.

## 0.1.0

- Added -u parameter for the units (metric, imperial).
- Changed the city name from optional argument to positional argument.

## 0.0.12

- Fixed missing 'light_rain' ASCII art.
- Fixed name 'light_rain' is not defined.
- Added Mist ASCII art.

[Unreleased]: https://github.com/egargo/pwygit/compare/2.1.2...HEAD
[2.1.2]: https://github.com/egargo/pwygit/compare/1.4.5...2.1.2
[1.4.5]: https://github.com/egargo/pwygit/compare/1.4.4...1.4.5
[1.4.4]: https://github.com/egargo/pwygit/compare/1.4.3...1.4.4
[1.4.3]: https://github.com/egargo/pwygit/compare/1.4.2...1.4.3
[1.4.2]: https://github.com/egargo/pwygit/compare/1.4.0...1.4.2
[1.4.0]: https://github.com/egargo/pwygit/releases/tag/1.4.0
