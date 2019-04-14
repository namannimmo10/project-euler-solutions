#code created by NamanNimmo Gera
#11:33am, April 14, 2019.

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

count = 0
for i in range(2,1000000+1):
    if not isPrime(i): continue
    combo = str(i)
    for j in range(len(combo)):
        combo = combo[-1] + combo[:-1]
        if not isPrime(int(combo)): break
    else:
        count += 1
print(count)
