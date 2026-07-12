import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Group data
category = df.groupby("product_category")["quantity_sold"].sum()

# Bar Plot
plt.bar(category.index, category.values)

# Title and Labels
plt.title("Products Sold by Category")
plt.xlabel("Product Category")
plt.ylabel("Quantity Sold")

# Rotate category names
plt.xticks(rotation=45)
plt.tight_layout()
# Show Graph
plt.show()