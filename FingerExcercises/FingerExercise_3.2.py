# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:26:13 2022

@author: bobby
"""

s = '1.23,2.4,3.123'
s = [float(idx) for idx in s.split(',')]
print(s)
total = 0
for c in s:
    total = total + c
print(total)