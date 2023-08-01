import webbrowser
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import ydata_profiling as pp
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("winequality-red.csv")

# print("Data head", end = "\n\n")
# print(df.head(), end = "\n\n")

# print("Data info", end = "\n\n")
# print(df.info(), end = "\n\n")

# print("Data describtion", end = "\n\n")
# print(df.describe(), end = "\n\n")

# # Generate the profile report
# profile = pp.ProfileReport(df, title = 'Pandas Profiling Report')

# # Save the report as HTML file
# profile.to_file("profile_report.html")

# # Open the report in the default web browser
# webbrowser.open("profile_report.html")

df = df.drop_duplicates()

from scipy.stats import zscore
df['z'] = zscore( df.quality )
df[ (df.z > 3.0) | (df.z < -3.0) ]
print(df.info(), end = "\n\n")

# # Calculate the correlation matrix
# correlation_matrix = df.corr()
# print(correlation_matrix)
# # Plot the correlation heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()

# target_corr = correlation_matrix['quality']
# print(target_corr)
# print(target_corr.sort_values(ascending=False))

# plt.scatter(df['alcohol'], df['quality'])
# plt.ylabel('quality')
# plt.xlabel('alcohol')
# plt.title('quality Against alcohol')
# plt.show()

# plt.scatter(df['volatile acidity'], df['quality'])
# plt.ylabel('quality')
# plt.xlabel('volatile acidity')
# plt.title('quality Against volatile acidity')
# plt.show()

# plt.scatter(df['volatile acidity'], df['alcohol'])
# plt.ylabel('alcohol')
# plt.xlabel('volatile acidity')
# plt.title('alcohol Against volatile acidity')
# plt.show()

y = df["quality"]
x = df.drop("quality", axis = 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, shuffle = True, random_state = 1)

# norm = MinMaxScaler(feature_range = (0, 1))
# norm.fit(x_train)
# x_train = norm.transform(x_train)
# x_test = norm.transform(x_test)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
print("Linear Regression Performance:")
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R-squared:", r2)