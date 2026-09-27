import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = np.array([
    [20, 25000],
    [24, 30000],
    [28, 40000],
    [32, 50000],
    [36, 60000]
])

standard = StandardScaler()
minimum = MinMaxScaler()

a = standard.fit_transform(data)
b = minimum.fit_transform(data)

print("StandardScaler:")
print(a)

print("\nMinMaxScaler:")
print(b)
