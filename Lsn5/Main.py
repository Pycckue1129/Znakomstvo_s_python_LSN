import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
#  df = pd.read_csv('sample_data/california_housing_train.csv', sep = ';')  # вывод через разделитель

df.head()
df.tail()
df.shape
df.isnull()
df.isnull().sum()
df.dtypes
df.columns
df['latitude']
print(df['latitude'])
print(df['population'])
df[['latitude', 'population']]
df[df['housing_median_age'] < 20]
df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]
df[df['housing_median_age'] < 20, 'total_rooms']
df[df['housing_median_age'] < 20, ['total_bedrooms', 'total_rooms']]
print(df['population'].max())
print(df['population'].min())
print(df['population'].mean())
print(df['population'].sum())
df[['population', 'total_rooms']].median()
df.describe()
