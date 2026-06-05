import pandas as pd  # importing pandas library

student_names = ["Tarun", "Anish", None, "Satvika", "Bairagi", "Uday"]  # some names contain missing values
student_marks = [85, None, 45, 90, None, 48]  # some marks contain missing values
student_city = ["Chennai", "Mumbai", "Delhi", None, "Bangalore", "Pune"]  # some cities contain missing values

student_details = {  # creating dictionary
    "Name": student_names,
    "Marks": student_marks,
    "City": student_city
}

student_df = pd.DataFrame(student_details)  # converting dictionary into dataframe

print("ORIGINAL DATAFRAME")
print(student_df)

print("\nMissing Values Before Cleaning")  # checking missing values
print(student_df.isnull().sum())

student_df["Name"] = student_df["Name"].fillna("Unknown")  # replacing missing names

student_df["City"] = student_df["City"].fillna("Unknown")  # replacing missing cities

average_marks = student_df["Marks"].mean()  # finding average marks

student_df["Marks"] = student_df["Marks"].fillna(average_marks)  # replacing missing marks

print("\nDATAFRAME AFTER CLEANING")
print(student_df)

print("\nMissing Values After Cleaning")
print(student_df.isnull().sum())

print("\nProgram Executed Successfully")
