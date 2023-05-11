#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:35:53 2022

@author: simenlogstein
"""

list1 = [5, 2, 9, 13423, 1, 6]


for i in list1:
    y = -1
    z = 0

    while z < len(list1) - 1:
        if list1[y+1] > list1[z+1]:
            list1[y+1], list1[z+1] = list1[z+1], list1[y+1]
        y = y+1
        z = z+1


print(list1)


