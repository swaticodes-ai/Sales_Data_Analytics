import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Calculate total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Display data
print("Sales Data:")
print(df)

# Total sales
total_sales = df["Total_Sales"].sum()
print("\nTotal Sales:", total_sales)

# Best-selling product
product_sales = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold by Product:")
print(product_sales)

best_product = product_sales.idxmax()
print("\nBest-Selling Product:", best_product)

# Sales by region
region_sales = df.groupby("Region")["Total_Sales"].sum()

print("\nTotal Sales by Region:")
print(region_sales)

# Product chart
product_sales.plot(kind="bar")

plt.title("Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

plt.tight_layout()
plt.show()
# Region-wise sales chart
region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# Total sales for each product
product_revenue = df.groupby("Product")["Total_Sales"].sum()

print("\nTotal Sales by Product:")
print(product_revenue)

# Product generating the highest revenue
highest_revenue_product = product_revenue.idxmax()

print("\nHighest Revenue Product:", highest_revenue_product)
# Revenue by Product chart
product_revenue.plot(kind="bar")

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.tight_layout()
plt.show()
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate monthly sales
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Total_Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)
# Monthly sales trend chart
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Category-wise sales
category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nTotal Sales by Category:")
print(category_sales)

# Best-performing category
best_category = category_sales.idxmax()

print("\nBest-Performing Category:", best_category)
# Find the region with the highest sales
best_region = region_sales.idxmax()

print("\nBest-Performing Region:", best_region)
