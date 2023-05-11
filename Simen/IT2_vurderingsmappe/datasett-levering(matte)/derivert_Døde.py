#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:21:01 2022

@author: simenlogstein
"""

from pylab import *
import pandas
import numpy as np
import matplotlib.pyplot as plt

datasett = pandas.read_excel('Italy.xlsx')

#print(datasett['Tid'])

plot(datasett['Dager'], datasett['Dode'])

Dager = datasett['Dager'].values

Dode = datasett['Dode'].values


plot(Dager, Dode, label="Døde")
title('Døde')
xlabel('Dager')
ylabel('døde av korona')
legend()

k = 30
start = k
slutt = len(Dager)-k

Dager_2 = []

Dode_liste = []


for i in range(start, slutt):
    Dager_2.append(Dager[i])
    Dode_liste.append(mean(Dode[(i-k):(i+k)]))
    
plot(Dager_2, Dode_liste, label="glidende gjennomsnitt")
legend()
show()

derivert = []   #verdier for den deriverte
Dager3 = [] #årstall som passer


for i in range(0, len(Dager_2)-1):
    delta_y = Dode_liste[i+1]-Dode_liste[i]
    delta_x = Dager_2[i+1] - Dager_2[i]
    
    derivert.append(delta_y / delta_x)
    Dager3.append(Dager_2[i])
     
plot(Dager3, derivert, label="deriverte av døde")
xlabel("Dager")
ylabel("stigningstall")
legend()
grid()
show()