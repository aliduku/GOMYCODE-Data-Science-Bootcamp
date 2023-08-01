import pandas as pd

data = [1,2,3,4,5]
index = ['A', 'B', 'C','D','E']
series_pd = pd.Series(data, index)
print("Original Data Series:")
print(series_pd, end = '\n\n')

index = ['E', 'D', 'C', 'B', 'A']
series_pd = series_pd.reindex(index)
print("Data Series after changing the order of index:")
print(series_pd)