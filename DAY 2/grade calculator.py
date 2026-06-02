count=1

def get_marks(marks):
    if marks>=90:
        print("A")
    elif marks>=75:
        print("B")
    elif marks>=60:
        print("C")
    elif marks>=45:
        print("D")
    else:
        print("F")
while(count<=5):
    marks=int(input("enter the marks:"))
    get_marks(marks)
    count+=1
