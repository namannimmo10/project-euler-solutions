#code created by NamanNimmo Gera
#3:50pm, April 10, 2019. 
import math

def findsum(num): #this is the function to find the sum of the proper divisors
    result = 0
    i = 2
    while i<= (math.sqrt(num)) : 
        if (num % i == 0) : 
            if (i == (num / i)) : 
                result = result + i; 
            else : 
                result = result +  (i + num/i); 
        i = i + 1
    return (result + 1); 

tot = 0 #this tot will be the final sum that we wanna calculate

for i in range(1,10000):
    a = findsum(i)
    b = findsum(a)
    if a != b: #this condition is also mentioned in the question
        if b == i:
            tot = tot + i
        
print(tot)        
