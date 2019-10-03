import math


def prime_check(n):
    prime = False

    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
            else:
                prime = True
    return prime


primes = [2]
n = 3

while True:
    if prime_check(n):
        primes.append(n)
    else:
        for i in primes:
            if math.sqrt(((n - i) / 2)) == int(math.sqrt(((n - i) / 2))):
                break
        else:
            print(n)
            break

    n += 2
