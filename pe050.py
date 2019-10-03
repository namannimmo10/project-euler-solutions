def sieve(n):
    # Sieve of Erotosthenes
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

# Driver code
length = 0 # length
largest = 0 # value
primes = sieve(1000000) # max_limit

lastelem = len(primes)

for i in range(len(primes)):
    for j in range(i+length, lastelem):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastelem = j+1
            break

# final result
print("Solution:", largest)
