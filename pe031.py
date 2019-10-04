target_balance = 200                              
denominations = [1, 2, 5, 10, 20, 50, 100, 200]   
ways_n = [0] * (target_balance + 1)               
ways_n[0] = 1                                     # Nos. of ways of creating 0 maybe 0 but for calculation we are taking it as 1 

                                                  
for i in denominations:                           # Running a loop of all denominations so as to calculate the number of ways each of them make a number
    for j in range(i,target_balance+1):           # Running a loop from 0 to 200 to update the number of ways each of them can be calculated
        ways_n[j] = ways_n[j] + ways_n[j - i]     # Calculating and adding number of ways in which i (current denomination) can calculate 0 to 200

print(ways_n[200])
