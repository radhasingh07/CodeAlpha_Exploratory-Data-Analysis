import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df.head())
print(df.info())
print(df.describe())

# -------------------------------
# Total Sales by Category
# -------------------------------
sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(10,6))
sales.plot(kind="bar", color=["skyblue","orange","green"])
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=300)
plt.show()

# -------------------------------
# Total Profit by Category
# -------------------------------
profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(10,6))
profit.plot(kind="bar", color=["skyblue","orange","green"])
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_category.png", dpi=300)
plt.show()

# -------------------------------
# Sales by Region
# -------------------------------
sales_region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(10,6))
sales_region.plot(kind="bar", color=["red","green","blue","orange"])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_by_region.png", dpi=300)
plt.show()

# -------------------------------
# Profit by Region
# -------------------------------
profit_region = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(10,6))
profit_region.plot(kind="bar", color=["purple","cyan","orange","green"])
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("profit_by_region.png", dpi=300)
plt.show()

# -------------------------------
# Top 10 Products by Sales
# -------------------------------
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(16,8))
top_products.plot(kind="bar", color="steelblue")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.xticks(rotation=35, ha="right", fontsize=9)
plt.tight_layout()
plt.savefig("top10_products_sales.png", dpi=300)
plt.show()

# -------------------------------
# Top 10 States by Sales
# -------------------------------
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top_states.plot(kind="bar", color="green")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("top10_states_sales.png", dpi=300)
plt.show()

# -------------------------------
# Top 10 Most Profitable Products
# -------------------------------
top_profit = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(16,8))
top_profit.plot(kind="bar", color="green")
plt.title("Top 10 Most Profitable Products")
plt.xlabel("Product Name")
plt.ylabel("Profit")
plt.xticks(rotation=35, ha="right", fontsize=9)
plt.tight_layout()
plt.savefig("top10_profitable_products.png", dpi=300)
plt.show()

# -------------------------------
# Top 10 Loss Making Products
# -------------------------------
bottom_profit = df.groupby("Product Name")["Profit"].sum().sort_values().head(10)

plt.figure(figsize=(16,8))
bottom_profit.plot(kind="bar", color="red")
plt.title("Top 10 Loss Making Products")
plt.xlabel("Product Name")
plt.ylabel("Profit")
plt.xticks(rotation=35, ha="right", fontsize=9)
plt.tight_layout()
plt.savefig("top10_loss_products.png", dpi=300)
plt.show()

# -------------------------------
# Discount vs Profit
# -------------------------------
plt.figure(figsize=(10,6))
plt.scatter(df["Discount"], df["Profit"], alpha=0.5, color="purple")
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("discount_vs_profit.png", dpi=300)
plt.show()