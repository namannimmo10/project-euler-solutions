#code created by NamanNimmo Gera
#11:39am, April 13, 2019.

import math

def reverse(s):  #function to reverse the string
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
    if (s == rev): 
        return True
    return False

tot=0 #this will be our final sum
for i in range(1,1000000):
    if isPalindrome(str(i)) and isPalindrome("{0:b}".format(i)):
        tot = tot + i
print(tot)        
