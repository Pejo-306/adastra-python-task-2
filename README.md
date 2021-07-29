# Adastra Python Task 2

This project is a simple ETL system, designed in *Python*, made for **Adastra Bulgaria**.

## Table of contents

* [Short description](#short-description)
* [Getting started](#getting-started)
    - [TL;DR](#tldr)
    - [Prerequisites](#prerequisites)
    - [Getting the project](#getting-the-project)
    - [Setting up a Python virtual environment](#setting-up-a-python-virtual-environment)
    - [Running the pseudo ETL system](#running-the-pseudo-etl-system)
    - [Running Python unit tests (Optional)](#running-python-unit-tests-optional)
* [Built with](#built-with)
* [License](#license)

## Short description

This project is an ETL script which extracts temperature data from *CSV* or *JSON* 
source files. The temperature is converted from Celsius to Fahrenheit and afterwards
is dumped into *CSV* or *JSON* formatted files.

The data (whether raw source or transformed) follows the following format when stored
in *CSV* format:
```csv
<city>,<timestamp>,<temperature value>
```
Example:
```csv
Sofia,2021-08-01T13:00:00+02:00,33 C
```

When formatted as *JSON*, the data is stored as an array of objects:
```json
[
  {
    "city": "<city>",
    "date": "<timestamp>",
    "temp": "<temperature value>"
  }
]
```
Example:
```json
[
  {
    "city": "Varna",
    "date": "2021-08-01T11:45:00Z",
    "temp": "25 F"
  }
]
```

## Getting started

This section contains instructions on how to download, setup and run the simple
ETL script.

### TL;DR

Clone the repo:
```bash
$ git clone https://github.com/Pejo-306/adastra-python-task-2
$ cd adastra-python-task-2/
```

(Optional | Recommended) Setup virtual environment (*venv*) and install requirements:
```bash
$ python3 -m venv ./venv
$ ./venv/bin/python3 -m pip install -r requirements.txt 
```

(Optional | Recommended) Run via virtual environment **Python 3** interpreter:
```bash
$ ./venv/bin/python3 main.py
```

Run via system's **Python 3** interpreter:
```bash
$ python3 main.py
```

### Prerequisites

You must have **Python3.8+** interpreter. This project was built with the following versions:

* Python 3.8.8

In [this](#setting-up-a-python-virtual-environment) section it is explained how 
to set up a Python virtual environment and install the necessary packages.

### Getting the project

To get a copy of the project, clone the repository like so:
```bash
$ git clone https://github.com/Pejo-306/adastra-python-task-2
$ cd adastra-python-task-2/
```

### Setting up a Python virtual environment

Whilst you can run the project via your system's **Python** interpreter, it is
generally discouraged to install third party libraries and to alter the system's
interpreter's version, as well as the system's packages' versions, to comply with
any project's version requirements. Therefore, it is advised to set up a **Python**
virtual environment with **Python's** built-in module *'venv'*.

To set up a virtual **Python 3** environment, run the following command:
```bash
$ python3 -m venv ./venv
```
which creates a virtual environment in the *'./venv'* directory. A **Python 3**
interpreter is now available in *'./venv/bin/python3'*.

Next, you can optionally install **Coverage.py** to test code coverage.
```bash
$ ./venv/bin/python3 -m pip install -r requirements.txt
```

### Running the pseudo ETL system

After a **Python** environment is set up, you may run the project as such 
(via virtual environment):
```bash
$ ./venv/bin/python3 main.py
```

Alternatively, you may run via the system's **Python 3** interpreter:
```bash
$ python3 main.py
```

A simple console front-end will ask for the input and output filepaths.
Both files must have either a *CSV* or *JSON* extension.

### Running Python unit tests (Optional)

You may run this project's **Python** unit tests with the following command
(from the project's root directory)*:
```bash
$ ./venv/bin/python3 -m unittest discover -s ./test/
```

Alternatively, via the system's **Python 3** interpreter:
```bash
$ python3 -m unittest discover -s ./src/tests/
```

Also, you can run **Coverage.py** to test for code coverage:
```bash
$ ./venv/bin/coverage run -m unittest discover -s ./test/
$ ./venv/bin/coverage report -m
```

## Built with

* [Python 3](https://www.python.org/)
    - [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)

## License

This project is distributed under the [MIT license](LICENSE).
