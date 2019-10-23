#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:17:19 2019

@author: dillu546
"""
d = {0: [1, 2, 3, 4, 5, 6], 1: [1, 2], 2: [3, 2, 7, 5, 6], 3: [3, 2, 7, 1, 6], 4: [4, 7, 2, 1],
     5: [3, 4, 7, 1, 6], 6: [3, 4, 5, 6, 1, 7], 7: [3, 2, 1], 8: [1, 2, 3, 4, 5, 6, 7], 9: [1, 2, 3, 4, 6, 7]}

d1 = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
for _ in range(int(input())):
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    v1 = d1.get(x[0])
    if v1 < y[0]:
        print('invalid')
    else:
        print(v1 - y[0], 7 - y[0])

