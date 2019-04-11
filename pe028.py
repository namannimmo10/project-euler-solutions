
#code created by NamanNimmo Gera
#9:07pm, april 9, 2019

tot = 0
i = 1001
while i>1:
    p = i*i
    q = i - 1
    tot = tot + (4*p)-(6*q)
      #(4*p - 6*q) = p +  p-q  +  p-2*q  +  p-3*q
    i = i-2
print(tot+1)
    
