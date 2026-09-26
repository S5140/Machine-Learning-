import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)

corr = df.corr()

sns.heatmap(corr, annot=True)
plt.show()

corr = corr.where(~(corr == 1))

print(corr.stack().idxmax())
print(corr.stack().max())
