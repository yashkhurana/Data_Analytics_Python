import pandas as pd

df = pd.read_csv("data/sales.csv")

print("Before Cleaning:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Missing Rows Remove
df_clean = df.dropna()

print("\nAfter Dropping Nulls:")
print(df_clean)

# Alternative: Fill missing values
df["Sales"].fillna(df["Sales"].mean(), inplace=True)
df["Profit"].fillna(0, inplace=True)



# Duplicate Remove
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)


# Sorting (Business Requirement)
# Highest sales first
sorted_df = df.sort_values(by="Sales", ascending=False)
print(sorted_df)


# Multiple column sort:

df.sort_values(by=["City", "Sales"], ascending=[True, False])

# Export Clean Data
df.to_csv("data/cleaned_sales.csv", index=False)

# Basic Visualization

pip install matplotlib

# import matplotlib.pyplot as plt

city_sales = df.groupby("City")["Sales"].sum()

plt.figure()
city_sales.plot(kind="bar")
plt.title("City Wise Total Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()
