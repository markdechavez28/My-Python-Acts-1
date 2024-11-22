import pandas as pd

data = {
    "Product": ["Laptop", "Smartphone", "TV", "Headphones", "Monitor", "Keyboard", "Mouse", "Speaker"],
    "Price": [1000, 700, 1500, 200, 800, 50, 25, 500],
    "Quantity": [5, 10, 3, 30, 4, 60, 100, 20]
}

df = pd.DataFrame(data)

price_mean = df['Price'].mean()
price_std = df['Price'].std()
quantity_mean = df['Quantity'].mean()
quantity_std = df['Quantity'].std()

df['Price'] = df['Price'].apply(lambda x: df['Price'].median() if abs((x - price_mean) / price_std) > 2 else x)
df['Quantity'] = df['Quantity'].apply(lambda x: df['Quantity'].median() if abs((x - quantity_mean) / quantity_std) > 2 else x)

print(df)
