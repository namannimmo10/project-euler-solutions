from datetime import date

count_sundays = 0

for year in range(1901, 2001):
	for month in range(1, 13):
		if date(year, month, 1).weekday() == 6:
			count_sundays += 1

print(count_sundays)
