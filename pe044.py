def find_pentagonal(n):
	return(n*(3*n - 1)//2)

def is_pentagonal(x):
	if (1 + (24*x +1)**0.5) % 6 == 0:
		return True
	else:
		return False

if __name__ == '__main__':
	
	i = 1 
	found = True
	while found:
		for x in range(1,i):
			a = find_pentagonal(i)
			b = find_pentagonal(x)
			if is_pentagonal(a+b) and is_pentagonal(a-b):
				print(abs(a-b))
				found = False
		i += 1
