#code created by Deepankar Agrawal(@deep110)
#11:04pm, October 03, 2019 UTC+05:30.

import math

"""
- make a list of all abundant numbers less than 28123
- then sum every combination of them to get list of numbers than can be
  written as sum of two abundant numbers
- Remove that set from set of numbers up-to 28123 and take sum.
"""

N = 28123

# find sum of divisors
def find_sum_divisors(num: int) -> int:
    if num == 1:
        return 1

    divisors_sum = 0
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            divisors_sum += i
            sec_div = int(num/i)
            if not (sec_div == i or sec_div == num):
                divisors_sum += sec_div

    return divisors_sum

def is_abundant(num: int) -> bool:
    return find_sum_divisors(num) > num

def build_abundant_list():
    abundant_nos = []
    for i in range(12, N+1):
        if is_abundant(i):
            abundant_nos.append(i)
    
    return list(set(abundant_nos))

def main():
    abundant_nos = build_abundant_list()

    # possible nos which can be written as sum of 2 abundant nos
    nos = []
    for i in abundant_nos:
        for j in abundant_nos:
            nos.append(i+j)

    # get nos that cannot be represented as sum
    nos_not_possible = set(range(1, N+1)) - set(nos)

    print(sum(nos_not_possible))

if __name__ == "__main__":
    main()