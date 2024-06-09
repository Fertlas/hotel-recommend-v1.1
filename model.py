import pandas as pd
from sklearn.preprocessing import MinMaxScaler # type: ignore
from sklearn.model_selection import train_test_split # type: ignore

df = pd.read_csv('terengganuhotels.csv')
df = df.dropna()

df = pd.get_dummies(df, columns=['District','Amenities'])

scaler = MinMaxScaler()
df[['price','rating']] = scaler.fit_transform(df[['price','rating']])

train_df, test_df = train_test_split(df, test_size= 0.2)