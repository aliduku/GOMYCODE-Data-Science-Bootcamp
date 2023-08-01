import pandas as pd

series = list(range(11))
series_pd = pd.Series(series)
print("Original Data Series:")
print(series_pd, end = '\n\n')

print("Subset of the above Data Series:")
print(series_pd[series_pd < 6])