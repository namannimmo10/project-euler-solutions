#code created by NamanNimmo Gera
#3:14pm, April 18, 2019.

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

def checkPerm(a,b,c):
    N1 = [int(i) for i in str(a)]
    N2 = [int(i) for i in str(b)]
    N3 = [int(i) for i in str(c)]
    N1.sort()
    N2.sort()
    N3.sort()
    if N1 == N2 == N3:
        string = ""
        string = string + str(a) + str(b) + str(c)
        return string


for i in range(1001,3338):
    if isPrime(i) and isPrime(i+3330) and isPrime(i + 2*3330):
        if checkPerm(i, i+3330, i + 2*3330):
            if i!=1487:
                print(checkPerm(i, i+3330, i + 2*3330))
                exit()
