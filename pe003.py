#code created by NamanNimmo Gera
#10:50am, April 11, 2019.

def largestPrime(num):
    i = 2
    while num % i != 0:
        i += 1
    if num % 2 == 0:
        if num == 2:
            return 2
        else:
            return largestPrime(num/2)
    elif num / i == 1:
        return num
    else:
        return largestPrime(num / i)


x = 600851475143
print(int(largestPrime(x)))
