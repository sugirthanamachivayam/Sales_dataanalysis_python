import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("sales_data.csv")

# Create Total_Sales column
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Total sales
total_sales = data["Total_Sales"].sum()
print("Total Sales:", total_sales)

# Sales by category
sales_by_category = data.groupby("Category")["Total_Sales"].sum()
print("\nSales by Category:")
print(sales_by_category)

# Top product by sales
top_product = data.groupby("Product")["Total_Sales"].sum().idxmax()
print("\nTop Product by Sales:", top_product)

# Plot chart
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()

# Save chart
plt.savefig("sales_by_category_python.png")
plt.show()