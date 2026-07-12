import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Group Data
region = df.groupby("customer_region")["total_revenue"].sum()

# Bar Plot
plt.bar(region.index, region.values)

# Title and Labels
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")

# Rotate Region Names
plt.xticks(rotation=45)
plt.tight_layout()
# Show Graph
plt.show()