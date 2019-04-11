#code created by NamanNimmo Gera
#8:12pm, April 11, 2019.

def checkpal(n):
    temp = n
    num = 0
    while temp>0:
        num = (num*10) + (temp%10)
        temp = temp//10
    if num==n:
        return True
    else:
        return False
        
z = 999
highest = 0
for i in range(z): #brute force rocks :p
    y = z-i
    for p in range(z):
        k = z - p
        if checkpal(k*y):
            if (k*y)>highest:
                highest = k*y
print(highest)
