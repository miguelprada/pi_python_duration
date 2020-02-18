#!/usr/bin/env python3
"""
@package pi_sample_duration
@file test_sample_duration.py
@author Anthony Remazeilles
@brief Compute an experiment duration based on a jointAngle File information

Copyright (C) 2020 Tecnalia Research and Innovation
Distributed under the Apache 2.0 license.

"""

import unittest
import os
from pi_sample_duration import compute_duration, store_result


TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'data/data_in.csv')


class PISampleDurationTest(unittest.TestCase):

    def test_bad_filename(self):
        self.assertEqual(compute_duration("whatever"), -1)

    def test_reference_data(self):
        self.assertNotEqual(compute_duration(TESTDATA_FILENAME), -1)

    def test_store(self):
        self.assertTrue(store_result("/tmp/out.yaml", 5))


if __name__ == '__main__':
    print("test_add -- begin")
    unittest.main()
    print("test_add -- end")
