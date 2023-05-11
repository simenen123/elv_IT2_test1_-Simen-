#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:25:31 2022

@author: simenlogstein
"""

from pylab import * 
from scipy.optimize import curve_fit
import pandas
import numpy as np

datasett = pandas.read_excel('Italy.xlsx')

Døde = datasett['Dode'].values

Friske = datasett['Recovery'].values

def f(x, a, b):
    return a*b**x


[a, b] = curve_fit(f, Døde, Friske)[0] # bestemmer a og b print("a =", round(a, 1))
print("a =", round(a, 1))
print("b =", b)

plot(Døde[0:559], Friske[0:559], "o") # plotter avfallsmengdene xlabel("År etter 1992")
xlabel("Døde")
ylabel("Friske")
x = linspace(0, 250000, 100)

plot(x, f(x, a, b), "r-") # plotter eksponentialfunksjonen show()