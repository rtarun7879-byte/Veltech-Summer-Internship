import pandas as pd  # importing pandas library

student_names = ["Tarun", "Anish", "Ovanish", "Satvika", "Bairagi", "Uday"]  # names

student_department = ["CSE", "CSE", "ECE", "ECE", "MECH", "MECH"]  # departments

student_marks = [85, 72, 45, 90, 55, 48]  # marks

student_details = {  # creating dictionary
    "Name": student_names,
    "Department": student_department,
    "Marks": student_marks
}

student_df = pd.DataFrame(student_details)  # creating dataframe

print("STUDENT DATA")
print(student_df)

print("\nAverage Marks Department Wise")

department_average = student_df.groupby("Department")["Marks"].mean()  # grouping by department

print(department_average)

highest_mark = student_df["Marks"].max()  # finding highest mark

print("\nHighest Mark Obtained =", highest_mark)

top_student = student_df[student_df["Marks"] == highest_mark]  # finding top student

print("\nTop Student Details")
print(top_student)

lowest_mark = student_df["Marks"].min()  # finding lowest mark

print("\nLowest Mark Obtained =", lowest_mark)

low_student = student_df[student_df["Marks"] == lowest_mark]  # finding lowest scoring student

print("\nLowest Scoring Student")
print(low_student)

print("\nProgram Executed Successfully")
