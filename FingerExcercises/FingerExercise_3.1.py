# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:05:50 2022

@author: bobby
"""

x = int(input('Enter an integer: '))
root = 0
pwr = 0

while root < abs(x):
    root = root+1
    for i in range(7):
        pwr = i
        if root**pwr == abs(x):
            break
    if root**pwr == abs(x):
        break
        print('Value of the decrementing function abs(x) - root**pwr is', abs(x) - root**pwr)
if root**pwr != abs(x):
    print(x, 'is not divisible by a power')
else:
    if x < 0 and pwr%2 != 0:
        root = -root
        print('Root is', root)
        print ('Power is', pwr)
    elif x < 0:
        print(x, 'is not divisible by a power')
    else:
        print('Root is', root)
        print ('Power is', pwr)
