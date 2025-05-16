import pandas as pd
df = pd.read_excel("listings.csv")


df.info(day=True, month=True, year_2023=True)

list(df.columns)
