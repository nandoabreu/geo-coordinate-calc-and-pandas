# Geo coordinate calculation (using pandas)

This task returns a list of trucks best located to be assigned to a cargo, based on geo coordinates from both, cargo and truck. This project was developed using **Python 3.8** over Ubuntu Linux and tested with _git clone_ into a Windows10 VirtualBox with Python 3.7.

&nbsp;  
&nbsp;  
## README Map

- Start with [Set-up and install](#set-up-and-install).
- For automatic tests, skip to [Automatic tests](#automatic-tests).
- To use the Truck class, skip to [The Truck class](#the-truck-class).
- To run from the command line, go to [Run from command line](#run-from-command-line).
- About logs, please move to the corresponding topic, [Logs](#logs).
- Instructions on advanced/technical documentation, go to [Documentation](#documentation).
- Or click to skip to the [To do](#to-do) list.


## Set-up and install
_I recommend using [virtualenv](https://realpython.com/python-virtual-environments-a-primer/)._

Install the requirements:

    $ python3 -m pip install -r requirements.txt

Please check the [config file](config.py) to personalise variables as needed.


## Automatic tests
_Note: to run tests manually, please refer to [Set-up and install](#set-up-and-install) first._

Python tests are available manually or using Makefile.  

- Run ` make test ` to setup, install requirements, run the tests and clean up.
- Or manually run ` python3 -m unittest tests/test_* `.


## The Truck class
_Note: to run from Python console, please refer to [Set-up and install](#set-up-and-install) first._

With the python console and the [Truck class](truck/__init__.py), we can get three best recommended trucks to transport a cargo, from the cargo's latitude and longitude:

    $ python3
    >>> from truck import Truck
    >>> t = Truck()
    >>> t.locate(36.876719, -89.5878579)


## Run from command line
_Note: to run from command line, please refer to [Set-up and install](#set-up-and-install) first._

From the project's root directory, please run the following command and follow instructions:

    $ python3 -m truck

_ATTENTION_: To **print all cargo** and **each optimal truck**, use the MENU option **_all_**.


## Logs
By default, logs are recorded in the 'logs' directory, in the project's root.

Please see [docs/logs](docs/logs) if you wish to access samples of the generated logs.


## Documentation
Please try from command line:

    $ python3 -c 'import config; help(config)'

Or try from python console:

    $ python3
    >>> import truck
    >>> help(truck)

All documentation can be found in [docs](docs).


## To do

* Preview distance between truck and load.
* Preview distance between cargo get and deliver point.
* Preview distance between truck and deliver.
* Configure rotation of log files.
* Improve docstrings.

