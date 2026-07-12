import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Top 10 Revenue Orders
top_orders = df.sort_values(by="total_revenue", ascending=False).head(10)

# Bar Plot
plt.figure(figsize=(10,5))
plt.bar(top_orders["order_id"].astype(str), top_orders["total_revenue"])

# Title and Labels
plt.title("Top 10 Revenue Orders")
plt.xlabel("Order ID")
plt.ylabel("Total Revenue")

# Rotate Labels
plt.xticks(rotation=45)

# Show Graph
plt.tight_layout()
plt.show()