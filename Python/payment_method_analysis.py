import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("../Dataset/amazon_sales_clean.csv")

# Count Payment Methods
payment = df["payment_method"].value_counts()

# Pie Chart
plt.pie(payment.values, labels=payment.index, autopct="%1.1f%%")

# Title
plt.title("Payment Method Distribution")

# Show Graph
plt.show()