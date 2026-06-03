import pandas as pd
name = ["Tarun", "Anish", "Ovanish", "Satvika", "Bairagi", "Uday"]            
age = [19, 20, 19, 18, 20, 21]
city = ["Chennai", "Mumbai", "Delhi", "Hyderabad", "Bangalore", "Pune"]
marks = [85, 72, 45, 90, 55, 48]
student_data = {
    "name": name,
    "age": age,
    "city": city,
    "marks": marks}
df = pd.DataFrame(student_data)# Converting dictionary into DataFrame
print("Student Information") # Displaying complete DataFrame
print(df)
print("\n")
print("First Five Records")# Displaying first 5 rows
head_data = df.head()
print(head_data)
print("\n")
row_count = df.shape[0]           # Finding number of rows and columns
column_count = df.shape[1]
print("Number of Rows =", row_count)        # Displaying rows and columns
print("Number of Columns =", column_count)
print("\n")
print("Shape of DataFrame")# Displaying shape of DataFrame
print(df.shape)
print("\n")
print("Data Types of Each Column") #displaying the data types
print(df.dtypes)
result = [] #creating empty result list
for mark in df["marks"]:#cheking either they are pass or fail
    if mark >= 50:
        result.append("Pass")
    else:
        result.append("Fail")
df["result"] = result
print("\n")
print("DataFrame After Adding Result Column")
print(df)
print("\n")
pass_count = 0#counting the passed and failed students
fail_count = 0
for value in df["result"]:
    if value == "Pass":
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1
#displaying pass and fail count in the dataframe
print("Total Passed Students =", pass_count)
print("Total Failed Students =", fail_count)
