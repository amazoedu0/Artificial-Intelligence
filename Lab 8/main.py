
#  *** ********* Task - 2 ********* ***

from random import *

a = []
b = []
c = []

stalls = ['food', 'cosmetics', 'garments', 'toys', 'shoes', 'jewelery']


def getTwoRandomValues():
    return sample(range(0, 5), 2)


def assignStallsToA():
    global c
    global b
    for stall in c:
        if stall not in b:
            a.append(stall)
    return a


def assignStallsToB():
    global c
    global b
    common = getTwoRandomValues()
    b = [stalls[common[0]], stalls[common[1]]]
    return b


def assignStallsToC():
    global c
    for stall in stalls:
        c.append(stall)
    return c


c = assignStallsToC()
b = assignStallsToB()
a = assignStallsToA()

print("STALLS IN A", a)
print("STALLS IN B", b)
print("STALLS IN C", c)
