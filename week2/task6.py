import os
import pandas as pd

# Create complete path
file_path = os.path.join(
    r"G:\Internship 2026\Intern_Nova\week2",
    "sales_data.csv"
)

# Check whether path exists
if os.path.exists(file_path):

    df = pd.read_csv(file_path)
    df["order_date"] = pd.to_datetime(df["order_date"])
    # print("File exists:", file_path)
# display original dataframe
    print("\nDisplay complete dataframe.")
    print(df)

# Display selected columns from the dataframe
    print("\nDisplay selected columns from the dataframe.")
    result = df[["order_id","order_date","product_category","quantity","unit_price"]].copy()
    result.insert(4,"total",df["quantity"]*df["unit_price"] )
    print(result)

    print("\nDisplay selected rows from the dataframe")
    print(result.tail(7))

# Filter record based on condition
    print("Filter record based on condition'latest 2026 orders'")
    latest_orders = (
        result.sort_values("order_date", ascending=False).head(3)
    )
    print(latest_orders)

# Apply multiple filtering conditions
    print("\nApply multiple filtering conditions 'Select orders where quantity is greater than 3 in 2022 year'")
    latest_2026_orders = (
        result[
            (result["quantity"] > 3) & 
            (result["order_date"].dt.year==2026)]
        .sort_values("order_date", ascending=False)
        .head(5)
    )
    print(latest_2026_orders)
# Sort data in ascending order.

    print("\n Sorting data in descending order based on product_cateogry")
    sorted_data_asc= (
            result.sort_values("product_category", ascending=True)
        )
    print(sorted_data_asc)
# Sort data in descending order.
    print("\n Sorting data in ascending order based on quantity")
    sorted_data_desc= (
            result.sort_values("quantity", ascending=False)
        )
    print(sorted_data_desc)

else:
    print("File does not exist:", file_path)