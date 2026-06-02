attampts=0
correct_password=1234

while(attampts<3):
    password=int(input("enter the password"))
    if password==correct_password:
        print("Acess granted")
        break
    else:
        print("Acess denied")
        
    attampts+=1
