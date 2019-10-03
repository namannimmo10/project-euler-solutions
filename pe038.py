def pandigital_multiples():
	n = int(input("Enter the limit : "))
	number = int(input("Enter the integer : "))
	multiples = []
	strings = ''
	for i in range(1,n+1):
		multiples.append(number*i)
		strings+=str(number*i)

	digits = []
	found=0
	if len(strings) == 9:
		for i in range(len(strings)):
			if strings[i] not in digits and int(strings[i]) in range(1,10):
				digits.append(strings[i])
			else:
				found=1
	else:
		print("none found")
		exit()

	if found == 0:
		print("Answer : {}".format(strings))
	else:
		print("none found")

if __name__ == "__main__":
	pandigital_multiples()
