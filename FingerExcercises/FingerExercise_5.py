# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 21:34:33 2022

@author: bobby
"""

## 5.1 Tuples
t1 = ()
t2 = (1, 'two', 3)
print(t1)
print(t2)

3*('a', 2)

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print((t1 + t2))
print((t1 + t2)[3])
print((t1 + t2)[2:5])

def intersect(t1, t2):
    """Assumes t1 and t2 are tuples
    Returns a tuple containing elements that are in
    both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

def findExtremeDivisors(n1, n2):
    """Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and
    the largest common divisor of n1 and n2. If no common divisor,
    returns (None, None)"""
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)

## 5.2 Ranges
L = ['I did it all', 4, 'love']
for i in range(len(L)):
    print(L[i])
    
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
print('Univs =', Univs)
print('Univs1 =', Univs1)
print(Univs == Univs1)

print(Univs == Univs1) #test value equality
print(id(Univs) == id(Univs1)) #test object equality
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))

print('Ids of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1]))
print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))
Techs.append('RPI')

for e in Univs:
    print('Univs contains', e)
    print(' which contains')
    for u in e:
        print(' ', u)
        
L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

def applyToEach(L, f):
    """Assumes L is a list, f a function
    Mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
L = [1, -2, 3.33]
print('L =', L)
print('Apply abs to each element of L.')
applyToEach(L, abs)
print('L =', L)
print('Apply int to each element of', L)
applyToEach(L, int)
print('L =', L)
print('Apply factorial to each element of', L)
applyToEach(L, factR)
print('L =', L)
print('Apply Fibonnaci to each element of', L)
applyToEach(L, fib)
print('L =', L)