import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Histogram
#plt.figure(figsize=(8, 5))
plt.hist(df["rating"], bins=9, range=(1, 5.5), 
         color="steelblue", edgecolor="black", alpha=0.85)

# Title and Labels
plt.title("Rating Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Rating")
plt.ylabel("Number of Products")

# Gridlines for readability
plt.grid(axis="y", linestyle="--", alpha=0.5)

# Clean layout
plt.tight_layout()

# Show Graph
plt.show()