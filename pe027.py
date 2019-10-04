def prime_check(n):
    prime = False

    if n > 1:
        if n == 2:
            return True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
            else:
                prime = True

    return prime


prime_sieve_1k = [i for i in range(1000) if prime_check(i)]
prime_sieve_1k_copy = prime_sieve_1k[:]

_max = 0
jmi = 0

for i in prime_sieve_1k:
    for j in prime_sieve_1k:
        k = 0

        while True:
            res = k**2 + j * k + i
            if res not in prime_sieve_1k_copy:
                if prime_check(res):
                    prime_sieve_1k_copy.append(res)

                else:
                    if k - 1 > _max:
                        _max = k - 1
                        jmi = j * i
                    break
            k += 1

        k = 0
        while True:
            res = k**2 - j * k + i
            if res not in prime_sieve_1k_copy:
                if prime_check(res) and res > 0:
                    prime_sieve_1k_copy.append(res)
                else:
                    if k - 1 > _max:
                        _max = k - 1
                        jmi = -1 * j * i
                    break
            k += 1

print(jmi)