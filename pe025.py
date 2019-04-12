#code created by NamanNimmo Gera
#12:47pm, April 12, 2019.
    
highest = 1000000
a,b = 1,1
for i in range(3,highest):
    new = a + b
    if len(str(new)) == 1000:
        print(i) #this will print 4782 
        break
    else:
        a = b
        b = new
