import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_profiling as pp
import webbrowser

# Read the dataset
data = pd.read_csv("adult.csv")

# Generate the profile report
profile = pp.ProfileReport(data, title = 'Pandas Profiling Report')

# Save the report as HTML file
profile.to_file("profile_report.html")

# Open the report in the default web browser
webbrowser.open("profile_report.html")