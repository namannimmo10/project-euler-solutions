#code created by NamanNimmo Gera
#10:38pm, April 13, 2019.

tot=0
for i in range(1,1001):
    tot = tot + i**i
a = len(str(tot))    
print(str(tot)[a-10:])
