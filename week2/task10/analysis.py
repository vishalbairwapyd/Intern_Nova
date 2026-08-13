
import os
import pandas as pd

current_folder = os.path.dirname(os.path.abspath(__file__))

dataset_folder = os.path.join(
    current_folder,
    "dataset"
)

file_path = os.path.join(
    dataset_folder,
    "Superstore.csv"
)

if os.path.exists(file_path):
# load data from a .csv file
    print("file path: ", file_path )
    df = pd.read_csv(file_path, encoding="latin1")
    print(df.head())

# Data inspection
    print(df.shape) # output (rows, columns)
    df.info()
    print("\nIn the loaded dataset convert 'Order Date' and 'Ship Date' from 'str' to 'datetime")
    df["Order Date"] = pd.to_datetime(df['Order Date'])
    df["Ship Date"] = pd.to_datetime(df['Ship Date'])
    print(df)
    df.info()

    # Now get the statistical summary of data
    print("\nStatistical Summary of dataset: ")
    print(df.describe())

# Identifying and handling missing values.

    # Check is there any Null column 
    print("Check any column has null value: ")
    print(df.isnull().sum())

# Selecting and filtering data.
    product_df = df[['Product ID', 'Product Name', 'Sub-Category', 'Category', 'Sales', 'Quantity', 'Discount', 'Profit']]
    Customer_df = df[['Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State','Postal Code', 'Region']]
    order_df = df[['Order ID', 'Order Date', 'Ship Date', 'Ship Mode']]
    print(product_df,Customer_df,order_df)

# data filtering
    result = product_df[
        product_df['Category'] == 'Technology'
    ][['Product Name', 'Category', 'Sub-Category', 'Sales']]

    print(result)
# sorting data in 'descending order'
    print(result.sort_values('Sales', ascending=False))

# Performing GroupBy analysis.
    print("Get all the total sales by grouping 'sub-category' in each category")
    print(product_df.groupby(['Category','Sub-Category'])['Sales'].sum().reset_index())

# Creating at least one Pivot Table
    print("Sales in different Region Pivot")

    region_sales = df.pivot_table(
        index=['Region','State'],
        values='Sales',
        aggfunc='sum'
    )

    print(region_sales)

# Finding useful insights from the dataset.
    # Does discount affect profit
    discount_profit = df.groupby('Discount')['Profit'].agg(
        Average_Profit='mean',
        Total_Profit='sum',
        Orders='count'
    ).reset_index()

    print(discount_profit)
    # Which category has high sales but low profit?
    category_analysis = df.groupby('Category').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum')
    ).sort_values('Total_Sales', ascending=False)

    print(category_analysis)

# Now save processed data 
    working_dir = f"{os.getcwd()}\Intern_Nova\week2"
    export_dir = os.path.join(working_dir, "export")
    # Create export directory if it doesn't exist
    os.makedirs(export_dir, exist_ok=True)
    df.to_csv(os.path.join(export_dir,"processed_data.csv"), index=False)
    
else:
    print("Dataset is not found. Please execute 'download_dataset.py' file")

