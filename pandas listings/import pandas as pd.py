import pandas as pd
df = pd.read_csv("listings.csv")

df.head()

df.tail()

df.describe()

df.info(show_counts=True, memory_usage=True, verbose=True)

df.shape

df.columns  in range(0,6)

list(pd.date_range)

df[['name']]

df[['name', 'neighbourhood_group']]

'D:\pandas listings\Pandas.ipynb'