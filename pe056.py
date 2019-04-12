#code created by NamanNimmo Gera
#2:25pm, April 12, 2019.

import time #just to calculate the execution time of the program 
start = time.time()

############################  main code is here 
highest = 0
for i in range(90,100):
    for j in range(90,100): #another brute force :D
        if sum(map(int, str(i**j)))>highest:
            highest = sum(map(int, str(i**j)))
                #to calculate the sum of digits of the number(i**j)
print(highest)            
############################ logic ends here


end = time.time()
print(end-start)
