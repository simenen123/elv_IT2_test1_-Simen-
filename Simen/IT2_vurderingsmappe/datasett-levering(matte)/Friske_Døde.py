#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:33:30 2022

@author: simenlogstein
"""

from pylab import *
import pandas
import numpy as np
import matplotlib.pyplot as plt

datasett = pandas.read_excel('Italy.xlsx')

#print(datasett['Tid'])


Døde = datasett['Dode'].values

Friske = datasett['Recovery'].values

k = 1
start = k
slutt = len(Døde)-k

aarstall_2 = []

temp_snitt = []


for i in range(start, slutt):
    aarstall_2.append(Døde[i])
    temp_snitt.append(mean(Friske[(i-k):(i+k)]))


plot(Døde[0:560], Friske[0:560], label="Friske")
title('Friske som funksjon av døde')
xlabel('Døde')
ylabel('Friske')
legend()
show()

derivert = []   #verdier for den deriverte

aarstall3 = [] #årstall som passer


for i in range(0, len(aarstall_2)-1):
    delta_y = temp_snitt[i+1]-temp_snitt[i]
    delta_x = aarstall_2[i+1] - aarstall_2[i]
    
    derivert.append(delta_y / delta_x)
    aarstall3.append(aarstall_2[i])
     
plot(aarstall3[0:560], derivert[0:560])
grid()