# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:07:03 2019

@author: tanma
"""

import time,calendar

calendar.setfirstweekday(6)

def sundays(year):
    counter = 0
    for month in range(1,13):
        cal = calendar.monthcalendar(year,month)
        if cal[0][0]:
            counter += 1
    return counter

t = int(input().strip())
for a0 in range(t):
    n = [int(i) for i in input().split(" ")]
    ne = [int(i) for i in input().split(" ")]
    total = 0
    for i in range(n[0],ne[0]):
        total += sundays(i)
    print(total)