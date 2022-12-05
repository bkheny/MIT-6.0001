# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:38:14 2022

@author: bobby
"""

x = float(input("Enter number x: "))
y = float(input("Enter number y: "))
z = float(input("Enter number z: "))


if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x>y and x>z:
        print('x is the largest odd number')
    elif y>z:
        print('y is the largest odd number')
    else:
        print('z is the largest odd number')
elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    if x>y:
        print('x is the largest odd number')
    else:
        print('y is the largest odd number')
elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    if x>z:
        print('x is the largest odd number')
    else:
        print('z is the largest odd number')
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    if y>z:
        print('y is the largest odd number')
    else:
        print('z is the largest odd number')
elif x%2 != 0:
    print('x is the largest odd number')
elif y%2 != 0:
    print('y is the largest odd number')
elif z%2 != 0:
    print('z is the largest odd number')
else:
    print('There are no odd numbers')