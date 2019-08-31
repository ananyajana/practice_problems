#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 07:54:53 2019

@author: aj611
"""

#s1 = "i.like.this"
s1 = int(input())
#print(s1)
for i in range(s1):
    s2 = input()
    #print(s2)
    string = []
    words = s2.split('.')
    #print(words)
    for word in words:
        string.insert(0, word)
    print('.'.join(string))