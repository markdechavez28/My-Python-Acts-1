import pandas as pd

data = {
    "Product": ["Laptop", "Laptop", "Smartphone", "smartphone", "TV", "tv", "Headphones", "headphones"],
    "Category": ["Electronics", "electronics", "Electronics", "electronics", "Electronics", "electronics", "Electronics", "electronics"],
    "Price": [1000, 1200, 700, 750, 1500, 1400, 200, 250],
    "Quantity": [5, 3, 8, 10, 2, 4, 15, 12]
}

df = pd.DataFrame(data)

df['Category'] = df["Category"].str.title()

df['Product'] = df["Product"].str.title()

df.drop_duplicates(keep="first")

print(df)