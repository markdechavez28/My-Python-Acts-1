import pandas as pd

data = {
    "Name": ["John", "Mary", "Alex", "Sarah", "Michael", "Laura", "David", "Anna"],
    "Age": [28, None, 30, 32, None, 25, 27, 29],
    "Salary": [50000, 60000, None, 70000, 80000, 45000, None, 55000],
    "Department": ["IT", "HR", "IT", None, "Marketing", "IT", "Marketing", None]
}

df = pd.DataFrame(data)

median = df['Age'].median()
df['Age'] = df['Age'].fillna(median)

mean = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean)

mode = df['Department'].mode()[0]
df['Department'] = df['Department'].fillna(mode)

df = df[df.isna().sum(axis=1) <= 2]

print(df)