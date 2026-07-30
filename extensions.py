import pandas as pd

df = pd.read_csv("sales.csv")
df["total_price"] = df["unit_price"] * df["units"]

total_revenue = df["total_price"].sum()
print(f"Total Revenue: {total_revenue:.2f}")

top_products = df.groupby("product")["total_price"].sum().nlargest(3)
print("\nTop 3 products:")
print(top_products.to_string())

revenue_per_region = df.groupby("region")["total_price"].sum()
print("\nRevenue per region:")
print(revenue_per_region.to_string())

df.to_csv("report_pandas.csv", index=False)
print("\nReport saved as report_pandas.csv")
