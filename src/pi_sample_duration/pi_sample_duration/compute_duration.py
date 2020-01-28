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

def compute_duration(file_ja_name):

    try:
        data = pd.read_csv(file_ja_name)
    except FileNotFoundError as err:
        print("Could not load file {}: {}".format(file_ja_name, err))
        return -1

    print("\n")
    print(data.head())
    
    if 'timestamp' not in list(data):
        print("Missing column timestamp")
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