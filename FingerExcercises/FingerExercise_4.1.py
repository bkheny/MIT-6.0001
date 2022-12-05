# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:48:22 2022

@author: bobby
"""
def isIn(x,y):
    if x in y:
        return 'true'
    elif y in x:
        return 'true'
    else:
        return 'false'

x = input('Enter x: ')
y = input('Enter y: ')
print(isIn(x,y))