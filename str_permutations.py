#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:03:37 2019

@author: aj611
"""

def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l == r:
        print(toString(a), end=' ')
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[i], a[l] = a[l], a[i]

s1 = int(input())
#print(s1)
for i in range(s1):
    s2 = input()
    n = len(s2)
    a = list(s2)
    permute(a, 0, n-1)
    print('\n')     