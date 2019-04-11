#code by NamanNimmo Gera
#6:06pm, april 9, 2019

list = []
 #creating an empty list 
 
for i in range(2,101):
    for j in range(2,101):
        if i**j not in list:
            list.append(i**j)
             
print(len(list))
 #the answer will be 9183 :)
