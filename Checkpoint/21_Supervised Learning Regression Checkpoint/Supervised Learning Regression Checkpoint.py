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
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("kc_house_data.csv")

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

# Calculate the correlation matrix
# correlation_matrix = df.corr()
# print(correlation_matrix)
# # Plot the correlation heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()

# target_corr = correlation_matrix['price']
# print(target_corr)
# print(target_corr.sort_values(ascending=False))

# plt.scatter(df['sqft_living'], df['price'])
# plt.ylabel('Price')
# plt.xlabel('sqft_living')
# plt.title('Price Against sqft_living')
# plt.show()

# plt.scatter(df['grade'], df['price'])
# plt.ylabel('Price')
# plt.xlabel('grade')
# plt.title('Price Against grade')
# plt.show()

# plt.scatter(df['sqft_above'], df['price'])
# plt.ylabel('Price')
# plt.xlabel('sqft_above')
# plt.title('Price Against sqft_above')
# plt.show()

# plt.scatter(df['sqft_living15'], df['price'])
# plt.ylabel('Price')
# plt.xlabel('sqft_living15')
# plt.title('Price Against sqft_living15')
# plt.show()

# plt.scatter(df['bathrooms'], df['price'])
# plt.ylabel('Price')
# plt.xlabel('bathrooms')
# plt.title('Price Against bathrooms')
# plt.show()

# plt.scatter(df['bedrooms'], df['price'])
# plt.ylabel('Price')
# plt.xlabel('bedrooms')
# plt.title('Price Against bedrooms')
# plt.show()

X = df[['sqft_living']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

fig = px.scatter(x=X_test['sqft_living'], y=y_test, title='Linear Regression')
fig.add_scatter(x=X_test['sqft_living'], y=y_pred, mode='lines', name='Regression Line')
fig.update_layout(title='Linear Regression', xaxis_title='sqft_living', yaxis_title='Price')
fig.show()

mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
print("Linear Regression Performance:")
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R-squared:", r2)

selected_features = ['sqft_living', 'grade']
X = df[selected_features]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

multi_linear_model = LinearRegression()
multi_linear_model.fit(X_train, y_train)

y_pred_multi = multi_linear_model.predict(X_test)

fig = go.Figure()
fig.add_trace(go.Scatter(x=X_test['sqft_living'], y=y_test, mode='markers', name='Actual'))
fig.add_trace(go.Scatter(x=X_test['sqft_living'], y=y_pred_multi, mode='lines', name='Multi-linear Regression'))
fig.update_layout(title='Multi-linear Regression', xaxis_title='sqft_living', yaxis_title='Price')
fig.show()

mse_multi = mean_squared_error(y_test, y_pred_multi)
rmse_multi = mean_squared_error(y_test, y_pred_multi, squared=False)
r2_multi = r2_score(y_test, y_pred_multi)
print("Multi-linear Regression Performance:")
print("Mean Squared Error:", mse_multi)
print("Root Mean Squared Error:", rmse_multi)
print("R-squared:", r2_multi)