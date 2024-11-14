import pandas as pd

df = pd.read_csv('dataset.csv')
df = df.head(10)
df = df.info()
df.fillna(0, inplace = True)
print(df)

data = {
    'Age': [22, 25, 29, 35, 40, 41, 60, 65],
    'Salary': [30000, 35000, 40000, 50000, 60000, 65000, 70000, 75000],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR']
}

df = pd.DataFrame(data)

print(df.describe())
print(df.describe(include='all'))
grouped = df.groupby('Department'['Age']).mean()

print(grouped)