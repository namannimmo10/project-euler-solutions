#code created by NamanNimmo Gera
#12:42pm, April 10, 2019.

from itertools import permutations
   #importing permutations :)

perm  = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for count, item in enumerate(perm):

 #to find the millionth permutation
    if count == 999999:     
        print(item)
        
