import pandas as pd

series = [100, 200, 'python', 300.12, 400]
series_pd = pd.Series(series)
print("Original Data Series:")
print(series_pd, end = '\n\n')

print("Sorted Data Series:")
series_pd = series_pd.astype(str)
series_pd = series_pd.sort_values()
print(series_pd)