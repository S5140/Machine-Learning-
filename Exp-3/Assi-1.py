import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

data = {
    "Age": [21, 24, None, 29, 32, 26],
    "Salary": [25000, None, 32000, 45000, 50000, 38000],
    "Department": ["IT", "HR", "IT", None, "Sales", "HR"],
    "Years of Experience": [1, 2, 4, None, 8, 3]
}

df = pd.DataFrame(data)

X = df[["Age", "Salary", "Department", "Years of Experience"]]

num = ["Age", "Salary", "Years of Experience"]
cat = ["Department"]

num_pipe = Pipeline([
    ("fill", SimpleImputer(strategy="median")),
    ("scale", StandardScaler())
])

cat_pipe = Pipeline([
    ("fill", SimpleImputer(strategy="most_frequent")),
    ("encode", OneHotEncoder(handle_unknown="ignore"))
])

preprocess = ColumnTransformer([
    ("num", num_pipe, num),
    ("cat", cat_pipe, cat)
])

result = preprocess.fit_transform(X)

print("Original Dataset:")
print(df)

print("\nProcessed Data:")
print(result)
