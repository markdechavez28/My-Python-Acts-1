import pandas as pd

data = {
    'id': ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010'],
    'name': ['John Doe', 'Jane Smith', 'Michael Johnson', 'Sara Lee', 'David Brown', 'Anna White', 'James Black', 'Emily Clark', 'Tom Harris', 'Lucy Green'],
    'age': [35, None, 27, 43, 38, 29, 32, None, 41, 27],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'rating': [4, 5, 3, 4, 2, 4, 1, 5, 3, None],
    'purchase': ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes'],
    'feedback': ['Great product, easy to use', 'Loved the design', 'Could be improved', 'Affordable and practical', 'Poor Quality', 'Good value for money', 'Not as expected', 'Excellent experience', 'Could use more features', 'Good price'],
    'date': ['2023-01-15', '2023-01-17', '2023-01-20', None, '2023-01-23', '2023-01-25', '2023-01-28', '2023-01-30', '2023-02-02', '2023-02-05']
}

df = pd.DataFrame(data)

age_mean = df['age'].mean()
df['age'] = df['age'].fillna(age_mean)

age_rating = df['rating'].mean()
df['rating'] = df['rating'].fillna(age_rating)

df = df.dropna(subset=['feedback'])

df['gender'] = df['gender'].replace({'Male': 'M', 'Female': 'F'})

df['date'] = pd.to_datetime(df['date'])

print(df)