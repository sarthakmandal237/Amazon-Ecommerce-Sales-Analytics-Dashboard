import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Select Numerical Columns
data = df[["price", "discount_percent", "quantity_sold", "rating", "review_count", "discounted_price", "total_revenue"]]

# Correlation
corr = data.corr()

# Heatmap
sns.heatmap(corr, annot=True)
#plt.tight_layout()

# Title
plt.title("Correlation Heatmap")

# Show Graph
plt.show()