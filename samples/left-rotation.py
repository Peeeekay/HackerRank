#!/bin/python

import sys

def leftRotation(a, d):
    # Complete this function

    length = len(a)
    count = 0
    i = 0
    tmp = a[i]
    temp = a[i]

    while count < (length):
        pos = (length + (i - d))%length
        tmp = a[pos]
        a[pos] = temp * -1
        if tmp >= 0:
            temp = tmp
            i = pos
            count = count + 1
        else:
            i = (pos + 1)%length
            temp = a[i]

    j=0
    while j < length:
        a[j] = a[j] * -1
        j = j + 1
    return a

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = map(int, raw_input().strip().split(' '))
    result = leftRotation(a, d)
    print " ".join(map(str, result))