#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:07:08 2022

@author: simenlogstein
"""

from pylab import * 
from scipy.optimize import curve_fit
import pandas
import numpy as np

datasett = pandas.read_excel('Italy.xlsx')

Dager = datasett['Dager'].values

Døde = datasett['Dode'].values

def f(x, a, b):
    return a*b**x


[a, b] = curve_fit(f, Dager, Døde)[0] # bestemmer a og b print("a =", round(a, 1))
print("a =", round(a, 1))
print("b =", round(b, 3))

plot(Dager, Døde, "o") # plotter avfallsmengdene xlabel("År etter 1992")
xlabel("Dager")
ylabel("Døde")
x = linspace(0, 950, 100)

plot(x, f(x, a, b), "r-") # plotter eksponentialfunksjonen show()