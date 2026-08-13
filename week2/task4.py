import pandas as pd

my_marks = pd.Series([60,98,55,99,87,89], index=["DBMS", "Python", "IOT", "Cloud", "DSA","Maths"])
# Series
print("##Created a Pandas Series ##")
print(my_marks)
print("Type of marks: ",type(my_marks))

print(my_marks["DBMS"])

# DataFrame
data = {
  "Students": ["Vishal", "Jatin", "Aman", "Ajay"],
  "Roll_No": range(1001,1005),
  "Marks": [99, 89, 100, 60]
}

students_details = pd.DataFrame(data)
print("\n##Created a Pandas DataFrame ##")
print(students_details)
print("Type of student_details: ",type(students_details))
print("\nDisplay the columns names of the dataframe: ", students_details.columns)
print("Display the index of dataframe: ", students_details.index)

print("\nAdd new gender column in dataframe")
print("## Old Dataframe ##")
print(students_details)
students_details.insert(1, "Gender", "M")
print("## Updated Dataframe ##")
print(students_details)

