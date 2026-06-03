import pandas as pd  # importing pandas library

student_names = ["Tarun", "Anish", "Ovanish", "Satvika", "Bairagi", "Uday"]  # names

student_age = [19, 20, 19, 18, 20, 21]  # ages

student_city = ["Chennai", "Mumbai", "Delhi", "Hyderabad", "Bangalore", "Pune"]  # cities

student_marks = [85, 72, 45, 90, 55, 48]  # marks

student_details = {  # creating dictionary
    "Name": student_names,
    "Age": student_age,
    "City": student_city,
    "Marks": student_marks
}

student_df = pd.DataFrame(student_details)  # creating dataframe

print("FULL EXPLORATORY DATA ANALYSIS REPORT")
print("-" * 60)

print("\nComplete DataFrame")
print(student_df)

print("\nShape of Dataset")
print(student_df.shape)

print("\nColumn Names")
print(student_df.columns)

print("\nData Types")
print(student_df.dtypes)

print("\nChecking Missing Values")
print(student_df.isnull().sum())

print("\nStatistical Summary")
print(student_df.describe())

print("\nMaximum Marks")
print(student_df["Marks"].max())

print("\nMinimum Marks")
print(student_df["Marks"].min())

print("\nAverage Marks")
print(student_df["Marks"].mean())

print("\nStudents Scoring Above Average")

average_marks = student_df["Marks"].mean()

above_average_students = student_df[student_df["Marks"] > average_marks]

print(above_average_students)

print("\nCity Wise Student Count")

city_count = student_df["City"].value_counts()

print(city_count)

print("\nProgram Executed Successfully")
