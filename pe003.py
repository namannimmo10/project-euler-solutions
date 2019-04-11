#code created by NamanNimmo Gera
#10:50am, April 11, 2019.

def largestPrime(num):
    j = 2
    while num % j != 0:
        j += 1
    if num % 2 == 0:
        if num == 2:
            return 2
        else:
            return largestPrime(num/2)
    elif num / j == 1:
        return num
    else:
        return largestPrime(num / j)


x = 600851475143
print(int(largestPrime(x)))
