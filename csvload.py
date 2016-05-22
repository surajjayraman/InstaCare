# -*- coding: utf-8 -*-
"""
Created on Wed May 04 18:59:58 2016

@author: Suraj
"""

import unicodecsv

with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    print enrollments[0]