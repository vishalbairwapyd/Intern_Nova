import os
import pandas as pd
# Create complete path
file_path = os.path.join(
    r"G:\Internship 2026\Intern_Nova\week2",
    "sales_data.csv"
)
# Check whether path exists
if os.path.exists(file_path):
    print("File exists:", file_path)
    # Read CSV
    df = pd.read_csv(file_path)
    print("Display the first 5 rows using head().")
    print(df.head(5))
    print("\nDisplay the last 5 rows using tail().")
    print(df.tail(5))
    # Check the number of rows and columns.
    print("\nCheck the number of rows and columns")
    n_rows, n_columns = df.shape
    print("In sales data there are {} rows and {} columns".format(n_rows, n_columns))

    print("\nDisplay column names: ")
    print(df.columns)
    print("\nCheck data types using dtypes.")
    print(df.dtypes)

    print("\nUse info() and describe() to understand the dataset.")
    df.info()
    df["order_date"] = pd.to_datetime(df["order_date"])
    print("\n Change order_date column 'str' to 'datetime': ")
    df.info()
    print()
    print(df.describe())
   
else:
    print("File does not exist:", file_path)

