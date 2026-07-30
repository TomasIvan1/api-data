import csv
from collections import defaultdict

total = 0.0
product_sales = defaultdict(float)

with open("sales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        revenue = float(row["unit_price"])*int(row["units"])
        total += revenue
        product_sales[row["product"]] += revenue

print(f"Total Revenue: {round(total, 2)}")

top = sorted(product_sales.items(), key=lambda item: item[1], reverse=True)[:3]
print("Top 3 products:")
for p in top:
    print(p[0])