#code created by NamanNimmo Gera
#7:54pm, April 28, 2019.

import time
start = time.time()

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
    
MAX = 500000    
prime_list = []
for i in range(2,MAX):
    if isPrime(i):
        prime_list.append(i)
print(prime_list[10000])        

end = time.time()
print(end-start)
