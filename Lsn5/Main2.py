import seaborn as sns

df = pd.read_csv('sample_data/california_housing_train.csv')

sns.scatterplot(data=df, x="longitude", y="latitude")
sns.scatterplot(data=df, x="households", y="population", hue="total_rooms")
sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
sns.relplot(x = 'longitude', y = 'median_house_value', kind = 'line', data = df)
sns.scatterplot(data=df, x="latitude", y="longitude", hue="median_house_value")
sns.histplot(data=df, x="median_income")
sns.histplot(data = df, x = 'housing_median_age')
sns.histplot(data=df[df['housing_median_age']>50], x="median_income")

df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50), 'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'

df.groupby('age_group')['median_income'].mean().plot(kind='bar')

df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'

sns.displot(df, x="median_house_value", hue="income_group")

