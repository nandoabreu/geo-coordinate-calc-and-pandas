#! /usr/bin/env python3
'''
Project's configuration file

This file holds necessary variables to this project.

Log variables:
    logs_level (str): Use one of CRITICAL, ERROR, WARNING, INFO, DEBUG
    logs_dir (str): Path to the logs directory
    logs_file (str): log filename to record in log_dir

Data (csv) confs:
    data_dir (str): Path to data (csv) files
    trucks_csv (str): trucks csv filename
    cargo_csv (str): cargo csv filename
'''

# Log variables:
logs_level = 'DEBUG'
logs_dir = 'logs'
logs_file = 'cargo.log'

# Data (csv) confs:
data_dir = 'data'
trucks_csv = 'trucks.csv'
cargo_csv = 'cargo.csv'


# Assure logs dir:
import os
os.makedirs(logs_dir, mode=0o777, exist_ok=True)

