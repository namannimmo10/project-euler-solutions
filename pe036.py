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

i = 1
tot=0 
while(i<1000000):
    if isPalindrome(str(i)) and isPalindrome("{0:b}".format(i)):
        tot = tot + i
    i = i + 2    #even number cannot be a palindrome ;)
print(tot)        
