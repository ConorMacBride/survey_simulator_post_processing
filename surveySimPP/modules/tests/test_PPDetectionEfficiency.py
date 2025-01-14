#!/bin/python

import pytest
import pandas as pd
import numpy as np
#from filtering import PPFilterDetectionEfficiencyThreshold

from surveySimPP.tests.data import get_test_filepath


"""
test_detectionEfficencyThreshold.py


Input:  1. file 'oiftrestoutput' 


Action: 1. count lines from raw output
        2. count lines after applying filter
        3. see if threshold is statistically solid
        
Author: Grigori Fedorets
"""


def test_PPDetectionEfficiency():

    from surveySimPP.modules.PPReadOif import PPReadOif
    from surveySimPP.modules.PPDetectionEfficiency import PPDetectionEfficiency

    rng = np.random.default_rng(2021)

    padafr = PPReadOif(get_test_filepath('oiftestoutput.txt'), 'whitespace')
    nrows = len(padafr.index)
    pada1 = PPDetectionEfficiency(padafr, 1.00, rng)
    nr1 = len(pada1.index)
    pada2 = PPDetectionEfficiency(padafr, 0.00, rng)
    nr2 = len(pada2.index)

    assert nr1 == nrows
    assert nr2 == 0

    return
