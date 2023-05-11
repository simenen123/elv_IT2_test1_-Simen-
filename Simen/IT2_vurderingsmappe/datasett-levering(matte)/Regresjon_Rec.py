#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:37:42 2022

@author: simenlogstein
"""

from pylab import * 
from scipy.optimize import curve_fit
import pandas
import numpy as np

datasett = pandas.read_excel('Italy.xlsx')

dager = datasett['Dager'].values

antall = datasett['Recovery'].values


def f(x, a, b, c):
    return c/(1 + a * exp(-b * x))

a_s = 1
b_s = 1
c_s = 1

[a, b, c] = curve_fit(f, dager[0:559], antall[0:559], p0 = [a_s, b_s, c_s])[0]


plot(dager[0:559], antall[0:559],"o")
plot(dager, f(dager, a, b, c), "r")
xlabel("dager")
ylabel("Friske")
show()

print("a =", round(a, 1))
print("b =", round(b, 2))
print("c =", round(c, 1))