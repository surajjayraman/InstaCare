# -*- coding: utf-8 -*-
"""
Created on Wed May 04 17:49:05 2016

@author: Suraj
"""


import matplotlib.pyplot as plt

xs = range(-30, 31)
ys = [x ** 2 for x in xs]

plt.scatter(xs, ys)
