import pandas as pd

data = {
    'Product': ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    'Sales': [200, 300, 400, None, 500, 600, None, 800, 900, 1000],
    'Cost': [150, 200, None, 250, 300, 350, 400, None, 500, 600],
    'Profit': [50, 100, 150, 200, None, 250, None, 400, 450, None]
}

df = pd.DataFrame(data)

mean = df['Sales'].mean()
df['Sales'] = df['Sales'].fillna(mean)

median = df['Cost'].median()
df['Cost'] = df['Cost'].fillna(median)

df['Profit'] = df['Profit'].fillna(0)

df.drop_duplicates()

Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.25 * IQR
upper = Q3 + 1.25 * IQR
df['Sales'] = df['Sales'].apply(lambda x: lower if x < lower else (upper if x > upper else x))

print(df)