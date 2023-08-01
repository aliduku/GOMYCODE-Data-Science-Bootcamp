import pandas as pd

data = [1,2,3,4,5,6,7,8,9,5,3]
series_pd = pd.Series(data)
print("Original Data Series:")
print(series_pd, end = '\n\n')

print("Mean = ", series_pd.mean())
print("Standard Deviation = ", series_pd.std())