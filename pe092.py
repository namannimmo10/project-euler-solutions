#code created by NamanNimmo Gera
#11:33pm, May 5, 2019.

#Edit : this solution is incomplete!

def compute(n):
    sum_ = 0
    while n:
        sum_ += (n % 10)*(n % 10)
        n = n // 10
    return sum_


nums_89 = set()
nums_1 = set()
for i in range(1, 10000000):
    numbers = set()
    j = i
    print('i', i)
    while j != 89 and j != 1 and j not in numbers:
        if j in nums_89:
            j = 89
            break
        elif j in nums_1:
            j = 1
            break
        numbers.add(j)
        j = compute(j)
        print('\tj', j)
    if j == 89:
        nums_89.add(i)
        nums_89 = nums_89 | numbers
    else:
        nums_1.add(i)
        nums_1 = nums_1 | numbers
print(len([i for i in nums_89 if i < 10000000]))
