results = set()
tokens = set('123456789')

# check for single digit multiplicand
for i in range(9):
    for j in range(999, 9999):
        s = str(i) + str(j) + str(i * j)
        
        if len(s) == 9 and set(s) == tokens:
            results.add(i * j)
        
        elif len(s) > 9:
            break

# check for double digit multiplicand
for i in range(9, 99):
    for j in range(99, 999):
        s = str(i) + str(j) + str(i * j)

        if set(s) == tokens:
            results.add(i * j)

        elif len(s) > 9:
            break

print(sum(results))
