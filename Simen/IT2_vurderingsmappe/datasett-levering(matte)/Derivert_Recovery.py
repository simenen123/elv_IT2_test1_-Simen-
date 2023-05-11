#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:09:44 2022

@author: simenlogstein
"""

from pylab import *
import pandas
import numpy as np
import matplotlib.pyplot as plt

datasett = pandas.read_excel('Italy.xlsx')


Dager = datasett['Dager'].values

Friske = datasett['Recovery'].values

plot(Dager[0:559], Friske[0:559], label="Friske")
title('Friske som funksjon av dager')
xlabel('dager')
ylabel('Friske')

k = 15
start = k
slutt = len(Dager)-k

aarstall_2 = []

temp_snitt = []

for i in range(start, slutt):
    aarstall_2.append(Dager[i])
    temp_snitt.append(mean(Friske[(i-k):(i+k)]))



plot(aarstall_2[0:500],temp_snitt[0:500], label="gjennomsnitt frisk")
title('Friske som funksjon av dager')
xlabel('dager')
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
     
title("Deriverte av Friske")
plot(aarstall3[0:500], derivert[0:500], label="stigningstall")
xlabel("Dager")
ylabel("stigningstall")
grid()