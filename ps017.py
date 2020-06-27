# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:20:28 2019

@author: tanma
"""

numbersDict = { 
0:"Zero",
1:"One",
2:"Two",
3:"Three",
4:"Four",
5:"Five",
6:"Six",
7:"Seven",
8:"Eight",
9:"Nine",
10:"Ten",
11:"Eleven",
12:"Twelve",
13:"Thirteen",
14:"Fourteen",
15:"Fifteen",
16:"Sixteen",
17:"Seventeen",
18:"Eighteen",
19:"Nineteen",
20:"Twenty",
30:"Thirty",
40:"Forty",
50:"Fifty",
60:"Sixty",
70:"Seventy",
80:"Eighty",
90:"Ninety"
}

def numberLetters(num):

    letters = ""

    if 0 < num <= 20:
        letters += numbersDict[num]

    if 21 <= num <= 99:
        a,b = divmod(num, 10)
        if b == 0:
            letters += numbersDict[a*10]
        else:
            letters += numbersDict[a*10] + " " + numbersDict[b]

    if 100 <= num <= 999:
        if num % 100 == 0:
            letters += numbersDict[int(num / 100)] + "Hundred"
        else:
            digit = int(num / 100)
            num = num - digit * 100
            if 0 < num <= 20:
                letters += numbersDict[digit] + "Hundred " + numbersDict[num]
            if 21 <= num <= 99:
                a,b = divmod(num, 10)
                if b == 0:
                    letters += numbersDict[digit] + "Hundred " + numbersDict[a*10]
                else:
                    letters += numbersDict[digit] + "Hundred " + numbersDict[a*10] + numbersDict[b]
    if num == 1000:
        letters += "One Thousand"

    return letters

t = int(input().strip())
for a0 in range(t):
    print(numberLetters(int(input())))

