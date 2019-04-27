#code created by NamanNimmo Gera
#8:15pm, April 27, 2019.

import time
start = time.time()

tot=2
a = 1
b = 2
while(b<4000000):
    a,b = b,a+b
    if b%2 == 0:
        tot = tot + b
print(tot)        

end = time.time()
print(end-start)
