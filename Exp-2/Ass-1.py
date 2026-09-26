import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["target"] = wine.target

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.duplicated().sum())

print(df.corr())

df.hist(figsize=(12, 10))
plt.show()
