import pandas as pd

# Dataset 1: Employee details
df1 = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104],
    "Name": ["Amit", "Rahul", "Priya", "Neha"],
    "Department": ["IT", "HR", "IT", "Sales"],
    "Salary": [50000, 40000, 60000, 45000]
})

# Dataset 2: Employee performance
df2 = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 105],
    "Performance": [85, 78, 92, 88],
    "Bonus": [5000, 4000, 7000, 6000]
})

# Merge Two DataFrames
print("Merged two dataframe df1 and df2")
merged_df = pd.merge(df1,df1, on="Employee_ID")
print(merged_df)

# Concatednate two dataframe df1 and df3
df3 = pd.DataFrame({
    "Employee_ID": [105, 106],
    "Name": ["Ravi", "Anjali"],
    "Department": ["Sales", "HR"],
    "Salary": [48000, 42000]
})

print("\nConcate two dataframe df1 and df3")
concated_df = pd.concat([df1, df3], ignore_index=True)
print(concated_df)

# Group By data based on a department column
print("\nGrouped data based on department and calculate each department total salary")
print(df1.groupby("Department")['Salary'].sum())


# Calculate aggregate values such as sum, mean, count, minimum, or maximum.
print("Calculate aggregate values such as sum, mean, count, minimum, or maximum.")
result = df1.groupby("Department")["Salary"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print(result)

# pivot table

pivot = pd.pivot_table(
    df1,
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print(pivot)

# Create a Pivot Table using Pandas.
# Summarize the data based on appropriate rows, columns, and values.
print("\nSummarize a pivot table data based on rows, column and values")

pivot = pd.pivot_table(
    df1,
    values="Salary",
    index="Department",
    aggfunc=["sum", "mean", "count"]
)

print(pivot)