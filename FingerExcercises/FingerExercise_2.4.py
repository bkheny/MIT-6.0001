# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:05:36 2022

@author: bobby
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
while (numXs != 0):
    toPrint = toPrint+'x'
    numXs = numXs - 1
print(toPrint)