"""
clean_data.py
Cleans and prepares the raw sales dataset for SQL analysis and Power BI.
Tools: Python, Pandas
"""

import pandas as pd

df = pd.read_excel("data/raw.xlsx", sheet_name="Raw_Sales_Data")

print(f"Raw shape: {df.shape}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Missing values:\n{df.isna().sum()[df.isna().sum() > 0]}")

# --- Cleaning steps ---

# 1. Remove exact duplicate rows (defensive — none found in this batch, but
#    this step is required for real-world sales exports which often have them)
before = len(df)
df = df.drop_duplicates()
print(f"Dropped {before - len(df)} duplicate rows")

# 2. Standardize text fields (trim whitespace, consistent casing)
text_cols = ["Customer_Name", "City", "State", "Category",
             "Sub_Category", "Product_Name", "Payment_Mode", "Gender"]
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

# 3. Correct dtypes
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Quantity"] = df["Quantity"].astype(int)
df["Age"] = df["Age"].astype(int)

# 4. Validate calculated fields (Sales = Unit_Price * Quantity * (1 - Discount))
expected_sales = (df["Unit_Price"] * df["Quantity"] * (1 - df["Discount"])).round(2)
mismatch = (df["Sales"].round(2) != expected_sales).sum()
print(f"Rows where Sales didn't match Unit_Price*Qty*(1-Discount): {mismatch}")

# 5. Feature engineering — useful fields for SQL grouping and Power BI slicers
df["Order_Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Order_Year"] = df["Order_Date"].dt.year
df["Profit_Margin_Pct"] = (df["Profit"] / df["Sales"] * 100).round(2)

# 6. Reorder columns sensibly
cols = ["Order_ID", "Order_Date", "Order_Month", "Order_Year", "Customer_ID",
        "Customer_Name", "Gender", "Age", "City", "State", "Category",
        "Sub_Category", "Product_Name", "Quantity", "Unit_Price", "Discount",
        "Sales", "Cost", "Profit", "Profit_Margin_Pct", "Payment_Mode"]
df = df[cols]

df.to_csv("outputs/sales_clean.csv", index=False)
print(f"\nFinal shape: {df.shape}")
print("Saved -> outputs/sales_clean.csv (load this into Power BI)")
