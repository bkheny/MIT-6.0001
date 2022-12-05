# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:01:02 2022

@author: bobby
"""

x = 27
epsilon = .01
numGuesses = 0
low = min(-1.0,x)
high = max(1.0,x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to the cubed root of', x)