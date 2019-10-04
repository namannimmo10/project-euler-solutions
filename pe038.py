def pandigital_multiples():
	answer = 0

	for i in range(1,10000):
		strings = ''

		index = 1
		while len(strings) < 9 :
			strings += str(i * index)
			index +=1

			if((len(strings) == 9) and (len(set(strings)) == 9) and ( '0' not in strings)):
				if int(strings) > answer:
					answer = int(strings)

	print(answer)


if __name__ == "__main__":
	pandigital_multiples()
