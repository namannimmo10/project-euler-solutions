#code created by NamanNimmo Gera
#10:54pm, April 11, 2019.

def count_terms(n): #function to find no of terms in the sequence
	if n <= 0: return 0
	c = 1
	while n > 1:
		n = n % 2 == 0 and n/2 or 3*n + 1
		c += 1
	return c

max = 0
start = 0
for x in range(1000001):
	c = count_terms(x)
	if c > max:
		max = c
		start = x
		
print(start)
