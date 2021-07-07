# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:42:15 2019

@author: tanma
"""

def recSumAtRow(rowData, rowNum):
    for i in range(len(rowData[rowNum])):
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    if len(rowData[rowNum])==1: 
        return rowData[rowNum][0]
    else: 
        return recSumAtRow(rowData, rowNum-1)


t = int(input().strip())
for a0 in range(t):
    n = input().strip()
    n = int(n)
    row = []
    for i in range(n):
        a = [int(i) for i in input().split(" ")]
        row.append(a)
    print(recSumAtRow(row, len(row)-2))