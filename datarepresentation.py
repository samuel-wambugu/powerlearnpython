import matplotlib.pyplot as mt
import seaborn as sns
import numpy as np

x = np.array([4500, 4566, 2345, 2346,7656,2555])
y = np.array([1,2,3,4,5,6])

mt.plot(y,x)

mt.ylabel("number of sales per day")
mt.xlabel("number of days")

df = sns.load_dataset('iris')

print(df.head())

mt.show()

x = np.random.normal(170, 10, 250)

mt.hist(x)
mt.show()