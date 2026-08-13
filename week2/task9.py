import pandas as pd
import os

working_dir = f"{os.getcwd()}\Intern_Nova\week2"
file_path = os.path.join(working_dir,"ecommerce_dirty_data.csv")
if os.path.exists(file_path):
    # print("You are in working directory")

# load data from the 'ecommerce_dirty_data.csv' file
    df = pd.read_csv(file_path)
    print(df)
# Process the data
    # Analyise imported data
    print("Analysis csv file data")
    df.info()
    print()

    # convert order_date column 'str' to 'datetime' object
    df['order_date'] = pd.to_datetime(df["order_date"])
    # again analyise data
    df.info()
    df.describe()

    # Identify missing values using isnull() / isna().
    print(df.isnull())
    # Count missing values in each column
    print("\n\ntotal null counts in each columns")
    print(df.isnull().sum())
    # Remove rows containing missing values.
    print("\nRemove rows containing missing values.")
    df_without_nan = df.dropna()
    print(df_without_nan)
    # display a dataframe where any single column contain null value
    # df[df.isnull().any(axis=1)]

    # Fill missing values using appropriate methods.
    print("First identify missing values")
    print(df.isnull().sum())
    # 1.handle 'order_date' missing values by (mean or median of order date)
    result_data = df.copy()
    result_data["order_date"] = result_data["order_date"].fillna(
        result_data["order_date"].mean()
    )
    print(f"Before 'order_date' column {df["order_date"].isnull().sum()} is missing")
    print(f"Now 'order_date' column {result_data["order_date"].isnull().sum()} is missing")
    # 2.handle 'customer_name' missing values by (mode or removing this column))
    result_data["customer_name"] = result_data["customer_name"].fillna(
            result_data["customer_name"].mode()[0]
        )
    print(f"Before 'customer_name' column {df["customer_name"].isnull().sum()} is missing")
    print(f"Now 'customer_name' column {result_data["customer_name"].isnull().sum()} is missing")
    # 3.Similarly handle [city, product cateogry, region, payment_method] missing values by (mode of that column))
    result_data["city"] = result_data["city"].fillna(result_data["city"].mode()[0])
    result_data["product_category"] = result_data["product_category"].fillna(result_data["product_category"].mode()[0])
    result_data["region"] = result_data["region"].fillna(result_data["region"].mode()[0])
    result_data["payment_method"] = result_data["payment_method"].fillna(result_data["payment_method"].mode()[0])

    # 4. Similarly handle [quantity, unit_price, discount, delivery_days, customer_rating] missing values by (median or mean)
    result_data["quantity"] = result_data["quantity"].fillna(result_data["quantity"].median())
    result_data["unit_price"] = result_data["unit_price"].fillna(result_data["unit_price"].median())
    result_data["discount"] = result_data["discount"].fillna(result_data["discount"].median())
    result_data["delivery_days"] = result_data["delivery_days"].fillna(result_data["delivery_days"].median())
    result_data["customer_rating"] = result_data["customer_rating"].fillna(result_data["customer_rating"].median())

    # 5. handle 'revenue' column missing values by this formulat 'quantity*unit_price*(1-discount/100)'
    result_data["revenue"] = (
    result_data["quantity"]
    * result_data["unit_price"]
    * (1 - result_data["discount"] / 100))
    # Display the dataset before and after handling missing values.
    print("\n\nBefore missing values data is like this: ")
    print(df.isnull().sum())
    print("\nAfter missing values data is like this: ")
    print(result_data.isnull().sum())


# Now save processed data 
    result_data.to_csv(os.path.join(working_dir,"processed_ecommerce_dirty_data.csv"), index=False)
    
# Verify that the exported file contains the processed data.
    file_path = os.path.join(working_dir,"processed_ecommerce_dirty_data.csv")
    if os.path.exists(file_path):
        df2 = pd.read_csv(file_path)
        print(df2)
    else:
        print("File does not exist:", file_path)
else: 
    print("File does not exist:", file_path)