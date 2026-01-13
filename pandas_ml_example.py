import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values
data = {
        'age': [25, 30, None, 22, 28, np.nan, 35],
        'salary': [50000, 60000, 55000, None, 70000, 65000, np.nan],
        'department': ['HR', 'Finance', 'IT', 'IT', None, 'Finance', 'HR'],
        'city': ['New York', None, 'Los Angeles', 'Chicago', 'New York', 'Chicago', 'Los Angeles'],
        'experience': [2, 5, 3, None, 7, 0, 6]
       }

df = pd.DataFrame(data)
# print("Original DataFrame with Missing Values:", df, sep="\n")


#First Thing ML Engineers Do: Inspect Data
df.head()
df.info()
df.describe()

# Handling missing values
# Fill missing numerical values with the mean of the column
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].median())
df['experience'] = df['experience'].fillna(df['experience'].mean())
# Fill missing categorical values with the mode of the column

# mode is the most frequently occurring value
df['department'] = df['department'].fillna(df['department'].mode()[0])
df['city'] = df['city'].fillna(df['city'].mode()[0])
# print("\nDataFrame after Handling Missing Values:", df, sep="\n")


# remove invalid data example age < 18
df = df[df['age'] >= 18]
print("\nDataFrame after Removing Invalid Data (age < 18):", df, sep="\n")