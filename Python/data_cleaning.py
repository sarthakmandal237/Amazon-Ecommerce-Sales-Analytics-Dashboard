# ==========================
# AMAZON SALES DATA CLEANING
# ==========================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# Load Dataset
# --------------------------

df = pd.read_csv("../Dataset/amazon_sales_dataset.csv")

# --------------------------
# Display First 5 Rows
# --------------------------

print("\nFirst 5 Rows:")
print(df.head())

# --------------------------
# Dataset Shape
# --------------------------

print("\nShape of Dataset:")
print(df.shape)

# --------------------------
# Column Names
# --------------------------

print("\nColumn Names:")
print(df.columns)

# --------------------------
# Dataset Information
# --------------------------

print("\nDataset Information:")
df.info()

# --------------------------
# Statistical Summary
# --------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------
# Random Sample
# --------------------------

print("\nRandom Sample:")
print(df.sample(5))

# --------------------------
# Missing Values
# --------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------
# Duplicate Rows
# --------------------------

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# --------------------------
# Data Types
# --------------------------

print("\nData Types:")
print(df.dtypes)

# --------------------------
# Convert Date Column
# --------------------------

df["order_date"] = pd.to_datetime(df["order_date"])

print("\nDate Column Converted Successfully!")

# --------------------------
# Clean Column Names
# --------------------------

df.columns = df.columns.str.strip().str.lower()

print("\nUpdated Column Names:")
print(df.columns)

# --------------------------
# Product Categories
# --------------------------

print("\nProduct Categories:")
print(df["product_category"].unique())

# --------------------------
# Save Clean Dataset
# --------------------------

df.to_csv("../Dataset/amazon_sales_clean.csv", index=False)

print("\nClean Dataset Saved Successfully!")