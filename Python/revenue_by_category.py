import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Dataset/amazon_sales_clean.csv")
category = df.groupby("product_category")["total_revenue"].sum()

plt.bar(category.index, category.values)
plt.title("Revenue by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()