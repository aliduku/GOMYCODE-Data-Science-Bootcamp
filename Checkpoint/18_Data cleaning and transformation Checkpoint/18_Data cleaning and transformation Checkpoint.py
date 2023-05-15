import pandas as pd
import pandas_profiling as pp
import webbrowser

# Read the dataset
data = pd.read_csv("covid_19_data.csv")

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