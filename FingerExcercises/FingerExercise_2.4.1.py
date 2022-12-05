# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 23:16:10 2022

@author: bobby
"""
count = 0
y = 'No odd number was entered'
while count <10:
    count = count + 1
    x = int(input('Input integer: '))
    if x %2 != 0:
        if y == 'No odd number was entered':
            y = x
        else:
            y = max(x,y)
if y == 'No odd number was entered':
    print(y)
else:
    print('The largest odd number is',y)
    