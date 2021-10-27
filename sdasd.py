import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

df = pd.DataFrame(dict(data=[2, 4, 1, 5, 9, 6, 0, 7]))
fig, ax = plt.subplots()

df['data'].plot(kind='bar', color='red')
df['data'].plot(kind='line', marker='*', color='black', ms=10)

plt.show()