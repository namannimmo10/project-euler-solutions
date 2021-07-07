# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:05:26 2019

@author: tanma
"""

import sys

def get_prod(x, k):
    n = list(str(x))
    l = [int(i) for i in n]
    prods = []
    for i in range(len(l)-k):
        a = 1
        for j in range(i,i+k):
            a *= l[j]
        prods.append(a)

    return max(prods) 


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(get_prod(num, k))