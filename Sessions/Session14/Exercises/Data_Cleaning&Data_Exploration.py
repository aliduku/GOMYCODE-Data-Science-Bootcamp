import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_profiling as pp
import webbrowser

# Read the dataset
data = pd.read_csv("baseball.csv")

# Generate the profile report
profile = pp.ProfileReport(data, title = 'Pandas Profiling Report')

# Save the report as HTML file
profile.to_file("profile_report.html")

# Open the report in the default web browser
webbrowser.open("profile_report.html")

# Handle missing values
data["RankPlayoffs"].fillna(0, inplace=True)
data["RankSeason"].fillna(0, inplace=True)
data["OSLG"].fillna(data["OSLG"].mean(), inplace=True)
data["OOBP"].fillna(data["OOBP"].mean(), inplace=True)

# Convert data types
data["Year"] = data["Year"].astype(int)
data["RankSeason"] = data["RankSeason"].astype(int)
data["Playoffs"] = data["Playoffs"].astype(int)
data["RankPlayoffs"] = data["RankPlayoffs"].astype(int)

# Check for duplicates and remove if any
data = data.drop_duplicates()

# Drop non-numeric columns
non_numeric_columns = ["Team", "League"]
data_numeric = data.drop(non_numeric_columns, axis=1)

# Calculate summary statistics
print("Summary Statistics:")
print(data_numeric.describe(), end = "\n\n")

# Find correlation and create heatmap
correlation = data_numeric.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Find top 5 teams with highest OBP and bottom 5 teams with lowest OBP
print("Top 5 Teams with Highest OBP:")
print(data.nlargest(5, "OBP")[["Team", "OBP"]], end = "\n\n")
print("Bottom 5 Teams with Lowest OBP:")
print(data.nsmallest(5, "OBP")[["Team", "OBP"]], end = "\n\n")

# Calculate average win percentage for teams that made the playoffs and those that didn't
print("Average Win Percentage for Teams that Made Playoffs:")
print(data.loc[data["Playoffs"] == 1, "W"].mean() / data.loc[data["Playoffs"] == 1, "G"].mean(), end = "\n\n")
print("Average Win Percentage for Teams that Made Playoffs:")
print(data.loc[data["Playoffs"] == 0, "W"].mean() / data.loc[data["Playoffs"] == 0, "G"].mean(), end = "\n\n")

# Group data by league and find average OBP and SLG for each league
print("Average OBP and SLG by League:")
print(data.groupby("League").agg({"OBP": "mean", "SLG": "mean"}), end = "\n\n")

# Generate the profile report
profile = pp.ProfileReport(data, title = 'Pandas Profiling Report')

# Save the report as HTML file
profile.to_file("profile_report.html")

# Open the report in the default web browser
webbrowser.open("profile_report.html")