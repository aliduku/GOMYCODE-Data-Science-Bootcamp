import pandas as pd
import plotly.express as px
import ydata_profiling as pp
import webbrowser

# Read the dataset
data = pd.read_csv("Video games.csv")

# Drop nan values
data = data.dropna(how="any")

# Convert year to int
data.Year = data.Year.astype(int)

# Sort the data by year
data = data.sort_values('Year')

# Get a quick overview of the data
print(data.head(), end = "\n\n")
print(data.info(), end = "\n\n")
print(data.describe(include = "all"), end = "\n\n")

# Look for missing values in the dataset.
print("Number of missing values:\n", data.isnull().sum(), end = "\n\n")

# Generate the profile report
profile = pp.ProfileReport(data, title = 'Pandas Profiling Report')

# Save the report as HTML file
profile.to_file("profile_report.html")

# Open the report in the default web browser
webbrowser.open("profile_report.html")

# Create an area chart to show the trend of global sales over the years
year_sales = data.groupby('Year')['Global_Sales'].sum().reset_index().sort_values('Year', ascending=False)
fig1 = px.area(year_sales, x='Year', y='Global_Sales')
fig1.update_layout(title='trend of global sales over the years', xaxis_title='Year', yaxis_title='Global Sales')
fig1.show()

# Create a histogram to show the distribution of global sales
fig2 = px.histogram(data, x='Year', y='Global_Sales', color='Year')
fig2.show()

# Create a scatter plot to show the relationship between North American sales and European sales
fig3 = px.scatter(data, x='NA_Sales', y='EU_Sales', color='Year')
fig3.update_layout(title='North American sales and European sales', xaxis=dict(title='NA Sales'), yaxis=dict(title='EU Sales'))
fig3.show()

# Create a scatter plot to show the relationship between Japanese sales and Other sales
fig4 = px.scatter(data, x='JP_Sales', y='Other_Sales', color='Year')
fig4.update_layout(title='Japanese sales and Other sales', xaxis=dict(title='NA Sales'), yaxis=dict(title='EU Sales'))
fig4.show()

# Create a stacked area chart to show the distribution of sales by platform over the years
year_platform_sales = data.groupby(['Year', 'Platform'])['Global_Sales'].sum().reset_index().sort_values('Year', ascending=False)
fig5 = px.area(year_platform_sales, x='Year', y='Global_Sales', color='Platform')
fig5.update_layout(title='Sales Distribution by Platform Over the Years', xaxis_title='Year', yaxis_title='Global Sales')
fig5.show()

# Create a bar chart to show the top 10 publishers by global sales
publisher_sales = data.groupby('Publisher')['Global_Sales'].sum().reset_index()
top_publishers = publisher_sales.sort_values('Global_Sales', ascending=False).head(10)
fig6 = px.bar(top_publishers, x = 'Publisher', y = 'Global_Sales')
fig6.update_layout(title='top 10 publishers by global sales', xaxis_title='Publisher', yaxis_title='Global Sales')
fig6.show()

# Create a pie chart to show the distribution of genres by global sales
fig7 = px.pie(data, values="Global_Sales", names='Genre', color='Genre', title='distribution of genres by global sales')
fig7.update_traces(textposition='inside', textinfo='percent+label')
fig7.update_layout(uniformtext_minsize=14)
fig7.show()