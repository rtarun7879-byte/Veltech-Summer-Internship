import numpy as np

number = int(input("Enter the number how many you want to enter"))             #asking the user for no of users

count = 1
marks = np.array([])                                                           #CREATING AN ARRAY TO ENTER THE MARKS

while(count <= number):
    times = int(input("Enter the numbers: "))                                  #In loop it ask marks of each student
    marks = np.append(marks, times)
    count = count + 1

print("Student Marks:")
print(marks)                                                                   #printing the array

average_marks = marks.mean()
print("\nAverage Marks =", average_marks)                                      #taking the mean marks=total number of students/number of students

highest_marks = marks.max()
print("Highest Mark =", highest_mark)                                          #taking the highest mark in the given array

lowest_marks = marks.min()
print("Lowest Mark =", lowest_mark)                                            #taking the lowest mark in the given array

std_deviation = marks.std()
print("Standard Deviation =", std_deviation)                                  # Calculating standard deviation

passing_students= 0                                                           #counting the number of students who got passed in the exam 

for mark in marks:
    if mark >= 50:
        passing_students = passing_students + 1

print("Number of Passed Students =", passing_students)
