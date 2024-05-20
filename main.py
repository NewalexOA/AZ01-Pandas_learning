import pandas as pd

kaggle_df = pd.read_csv('salaries.csv')
print(kaggle_df.head(5))
print(kaggle_df.info())
print(kaggle_df.describe())


df = pd.read_csv('dz.csv')
print(df.groupby('City')['Salary'].mean())