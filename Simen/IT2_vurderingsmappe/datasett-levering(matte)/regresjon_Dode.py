#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:20:07 2022

@author: simenlogstein
"""

from pylab import * 
from scipy.optimize import curve_fit
import pandas
import numpy as np

datasett = pandas.read_excel('Italy.xlsx')

dager = datasett['Dager'].values

antall = datasett['Dode'].values


def f(x, a, b, c):
    return c/(1 + a * exp(-b * x))

a_s = 164845
b_s = 0.047
c_s = 164846

[a, b, c] = curve_fit(f, dager, antall, p0 = [a_s, b_s, c_s])[0]

print("a =", round(a, 1))
print("b =", round(b, 2))
print("c =", round(c, 1))

plot(dager, antall,"o")
x = linspace(0, 1000, 1000)
xlabel("Dager")
ylabel("Døde")
plot(x, f(x, a, b, c), "r", label="Regresjon")
show()