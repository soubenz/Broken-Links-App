[![Build Status](https://travis-ci.com/thesamartian/Broken-Links-App.svg?branch=master)](https://travis-ci.com/thesamartian/Broken-Links-App)

# Broken Links Checker 

A broken links checker for websites. Enter your url and wait for the results ! 
The results are exported in your prefered format.

## Installation

The package depends on Peotry for dependecies management. It is imperative to have it installed.
To install Poetry:

```shell
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

or visit https://poetry.eustace.io/docs/ for more info.


You can install the package by following the next steps:

1. cloning the project from the remote repositry.
2. activate Poetry

```shell
source $HOME/.poetry/bin
```

3. Make sure you're in the project root and install the package dataimpact-scraping-launcher along with all the dependecies using the following command:

```shell
Poetry install
```

## Usage
The project is served using a CLI.
```shell
python broken_link_checker/launcher.py run http://example.com
```



### Options
Use flags to use a option

- **export**: export format. (CSV, JSON, XML)
- **export_dir**: export directory. default (/tmp)
- **obey**: obey robot.txt file. default(false)
- **debig**: activate debug.default(true)
- **log_dir**: debug log directory. default (/tmp)
- **useragent**: custom useragent. default (Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36)

## Tests
To run tests, you need to have Poetry installed

```shell
poetry run tox
```
