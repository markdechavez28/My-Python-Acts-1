import pandas as pd

data = {
    'id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'David Clark', 'Eva White', 'Frank King', 'Grace Lee', 'Hannah Turner', 'Ivy Wilson', 'Jack Scott'],
    'dept': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [50000, 60000, 55000, None, 62000, 70000, 52000, 59000, 1000000, 63000],
    'hire': ['2015-05-10', '2017-08-15', '2016-02-23', '2018-09-19', '2015-04-10', '2014-06-08', '2019-10-05', '2020-03-23', '2021-07-12', '2017-11-11'],
    'age': [34, 29, 42, 38, 30, 35, 28, 32, 36, 40],
    'bonus': [5000, 6000, 7000, 8000, 10000, 12000, 500000, 11000, 9000, 15000]
}

df = pd.DataFrame(data)

ave_salary = df['salary'].mean()
df['salary'] = df['salary'].fillna(ave_salary)

df['id'].drop_duplicates()

df['dept'] = df['dept'].str.upper()

bonus_mean = df['bonus'].mean()
bonus_sd = df['bonus'].std()
df['bonus'] = df['bonus'].apply(lambda x: None if abs((x - bonus_mean) / bonus_sd) > 2 else x)
df = df.dropna(subset=['bonus'])

df['hire'] = pd.to_datetime(df['hire'])

print(df)