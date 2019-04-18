#code created by NamanNimmo Gera
#6:40pm, April 18, 2019.

import time
start = time.time()
for i in range(1,1000000): #bruuuuuute force 
  if set(list(str(i))) == set(list(str(2*i))) == set(list(str(3*i))) == set(list(str(4*i))) == set(list(str(5*i))) == set(list(str(6*i))):
    print(i)
    break
end = time.time()
print(end-start)
