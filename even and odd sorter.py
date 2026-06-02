a=int(input("enter the numbers you want enter in the list"))
list=[]
even_list=[]
odd_list=[]
for i in range(1,a):
    b=int(input("enter the number"))
    list.append(b)
for i in list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)

    
    


    
    

