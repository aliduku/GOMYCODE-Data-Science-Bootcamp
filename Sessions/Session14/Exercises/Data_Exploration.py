# Import libraries
import pandas as pd
import pandas_profiling as pp
import webbrowser

# Step 1: Importing the data
data = pd.read_csv("Popular_Baby_Names.csv")

# Step 2: Exploring the data
# Get a quick overview of the data
print(data.head())
print(data.info())
print(data.describe())
print(data.describe(include = "all"))

# Step 3: Identifying and handling missing values
# Check for missing values
print(data.isnull())

# Generate the profile report
profile = pp.ProfileReport(data, title = 'Pandas Profiling Report')

# Save the report as HTML file
profile.to_file("profile_report.html")

# Open the report in the default web browser
webbrowser.open("profile_report.html")