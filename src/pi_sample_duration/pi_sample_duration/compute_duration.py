#!/usr/bin/env python3
"""
@package pi_sample_duration
@file compute_duration.py
@author Anthony Remazeilles
@brief Compute an experiment duration based on a jointAngle File information

Copyright (C) 2020 Tecnalia Research and Innovation
Distributed under the Non-Profit Open Software License 3.0 (NPOSL-3.0).

"""

# Used to handle csv file as dataframe
import pandas as pd
import sys
from termcolor import colored

def compute_duration(file_ja_name):

    try:
        data = pd.read_csv(file_ja_name)
    except FileNotFoundError as err:
        print(colored("Could not load file {}: {}".format(file_ja_name, err), "red"))
        return -1

    print("\n")
    print(data.head())
    
    if 'timestamp' not in list(data):
        print(colored("Missing column timestamp", "red"))
        return -1

    time_start = data.iloc[0]['timestamp']
    time_end = data.iloc[-1]['timestamp']

    duration = time_end - time_start

    return duration

def store_result(file_out, value):

    file = open(file_out, 'w')
    file.write('type: \'scalar\'\nvalue: [[' + format(value, '.5f') + ']]')
    file.close()

    return True

USAGE = """usage: run_pi file_in file_out
file_in: csv file containing at least a timestamp column
file_out: yaml file in which the sample duration wil lbe written
"""


def main():
    if len(sys.argv) != 3:
        print(colored("Wrong input parameters !", "red"))
        print(colored(USAGE, "yellow"))
        return -1

    file_in = sys.argv[1]
    file_out = sys.argv[2]

    duration = compute_duration(file_in)

    if duration == -1:
        return -1

    if not store_result(file_out, duration):
        return -1
    print (colored("duration: {} stored in {}".format(duration, file_out), "green"))
    return 0
