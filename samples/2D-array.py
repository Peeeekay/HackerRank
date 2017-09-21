#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

x = 1
y = 1
maxi = -10000

def hourGlassSum(x,y):
    one = arr[x-1][y-1]
    two = arr[x-1][y]
    three = arr[x-1][y+1]
    four = arr[x][y]
    five = arr[x+1][y-1]
    six = arr[x+1][y]
    seven  = arr[x+1][y+1]
    total = one + two + three + four + five + six + seven
    return total

for i in range(1,5):
    for j in range(1,5):
        temp = hourGlassSum(i,j)
        if temp >= maxi:
            maxi = temp

print maxi