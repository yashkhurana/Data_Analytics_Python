import pandas as pd

# Read CSV file
df = pd.read_csv(r"C:\Users\Yash.Khurana\Downloads\sales.csv")

print(df)

# Understand Data

print(df.head())    # Top 5 rows
print(df.tail())    # Last rows
print(df.shape)   # rows, columns
print(df.columns) # column names
print(df.info())    # data types


# Select Columns

print(df["OrderID"])
print(df["Sales"])

# selecting multiple columns

print(df[["OrderID","Sales","Customer"]])

print(df.head(2))

# Basic Calculations

print("The Total Sales is ",df["Sales"].sum())
print("Average Sales is ",df["Sales"].mean())
print("Count of OrderID ",df["OrderID"].count())
print("Max Sales is ",df["Sales"].max())
print("Min Sales is ",df["Sales"].min())

# Filter data

# delhi customers

print(df[df["City"] == "Delhi"])

salesdata = df[df["Sales"] == 800]

# high sales

highsales = df[ (df["Sales"] > 800) & (df["Profit"] > 300)]

print(highsales)

# Calculated Columns

df["Profit Percentage"] = (df["Profit"] / df["Sales"]) * 100

print(df)


#Group By Operation

city_wise_sales = df.groupby("City")["Sales"].sum().rename("Total Sales").reset_index()

print(city_wise_sales)
