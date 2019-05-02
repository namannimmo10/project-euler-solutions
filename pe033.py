#code created by NamanNimmo Gera
#11:07pm, May 2, 2019.

import math
#print(49//math.gcd(49,98))
 
def GCD(x, y):
    while(y):
        x, y = y, x % y 
    return x     
    
#print(str(49//GCD(49,98)) + "/" + str(98//GCD(49,98)))
def mathemagician(a,b):
    lsbA = a%10
    msbA = a//10
    lsbB = b%10
    msbB = b//10
    if lsbA==msbB:
        string = str(msbA//GCD(msbA,lsbB)) + "/" + str(lsbB//GCD(msbA,lsbB))
        return string
    elif lsbB==lsbA:
        string = str(msbA//GCD(msbA,msbB)) + "/" + str(msbB//GCD(msbA,msbB))
        return string
    elif msbA==msbB:
        string = str(lsbA//GCD(lsbA,lsbB)) + "/" + str(lsbB//GCD(lsbA,lsbB))
        return string
    elif msbA==lsbB:
        string = str(lsbA//GCD(lsbA,msbB)) + "/" + str(msbB//GCD(lsbA,msbB))
        return string
        
def mainLogic(a,b):
    string = str(a//GCD(a,b)) + "/" + str(b//GCD(a,b))
    return string


def checker(a,b):
    string1 = mainLogic(a,b)
    string2 = mathemagician(a,b)
    if string2==string1:
        return True
    
for i in range(11,100):
    if i%10 ==0:
        continue
    for j in range(i+1,100):
        if j%10 ==0:
            continue
        if checker(i,j):
            print(i,j)
print(str((16*19*26*49)//GCD(16*19*26*49,64*95*65*98)) +"/" +str((64*95*65*98)//GCD(16*19*26*49,64*95*65*98)))
#ANSWER IS 100 :)
