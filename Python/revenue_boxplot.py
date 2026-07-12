import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Box Plot
plt.boxplot(df["total_revenue"])

# Title and Labels
plt.title("Revenue Distribution")
plt.ylabel("Total Revenue")

# Show Graph
plt.show()