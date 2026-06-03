import pandas as pd  

student_names = ["Tarun", "Anish", "Ovanish", "Satvika", "Bairagi", "Uday"]                     # storing names
student_ages = [19, 20, 19, 18, 20, 21]                                                         # storing ages
student_cities = ["Chennai", "Mumbai", "Delhi", "Hyderabad", "Bangalore", "Pune"]               # storing cities
internet_access = ["yes", "yes", "no", "yes", "no", "yes"]                                      # internet availability
student_marks = [85, 72, 45, 90, 55, 48]                                                        # storing marks

student_details = {                                                                             # creating dictionary
    "Name": student_names,
    "Age": student_ages,
    "City": student_cities,
    "Internet": internet_access,
    "Marks": student_marks
}

student_df = pd.DataFrame(student_details)                                                     # converting dictionary into dataframe

print("STUDENT DATA ANALYSIS")                                                                 # displaying title
print("-" * 50)

total_rows = student_df.shape[0]                                                               # getting row count
total_columns = student_df.shape[1]                                                            # getting column count

print("\nNumber of Rows =", total_rows)                                                        # displaying rows
print("Number of Columns =", total_columns)                                                    # displaying columns
 
print("\nColumn Names")                                                                        # displaying column names

for column_name in student_df.columns:                                                         # traversing column names
    print(column_name)  

print("\nFirst 3 Records")                                                                     # displaying first 3 rows
first_records = student_df.head(3)
print(first_records)
 
print("\nLast 3 Records")                                                                      # displaying last 3 rows
last_records = student_df.tail(3)
print(last_records)

print("\nInternet Access Count")                                                               # counting internet values
internet_count = student_df["Internet"].value_counts()
print(internet_count)

students_with_internet = internet_count.get("yes", 0)                                          # counting yes
students_without_internet = internet_count.get("no", 0)                                        # counting no

print("\nStudents Having Internet =", students_with_internet)                                  # displaying yes count
print("Students Not Having Internet =", students_without_internet)                             # displaying no count
                  
print("\nProgram Executed Successfully")                                                       # ending message
