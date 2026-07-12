import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Histogram
#plt.figure(figsize=(8, 5))
plt.hist(df["discount_percent"], bins=10, 
         color="steelblue", edgecolor="black", alpha=0.85)

# Title and Labels
plt.title("Discount Percentage Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Discount Percentage")
plt.ylabel("Number of Orders")

# Gridlines for readability
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Clean layout
plt.tight_layout()

# Show Graph
plt.show()