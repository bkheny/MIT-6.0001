# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:34:43 2022

@author: bobby
"""

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
k = .5
guess = k/2.0
numGuesses_Newton = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuesses_Newton +=1
print('Number of Newton-Rhapson guesses:', numGuesses_Newton)
print('Square root of', k, 'is about', guess)

numGuesses = 0
low = min(-1.0,k)
high = max(1.0,k)
ans = (high + low)/2.0
while abs(ans**2 - k) >= epsilon:
    numGuesses += 1
    if ans**2 < k:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Number of bisection guesses =', numGuesses)
print('Suqre root of',k, 'is about', ans)