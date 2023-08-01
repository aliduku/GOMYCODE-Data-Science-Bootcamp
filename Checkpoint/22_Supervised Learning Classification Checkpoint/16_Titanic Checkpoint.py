import pandas as pd

# Read the dataset
data = pd.read_csv("titanic-passengers.csv", delimiter = ';')

# Get a quick overview of the data before preprocessing
print("Summary before preprocessing:")
print("Summary Datatypes:\n", data.info(), end = "\n\n")
print("Summary Statistics:\n", data.describe(include = "all"), end = "\n\n")

# Check for duplicates and remove if any
data = data.drop_duplicates()

# Handle missing values: Age can be filled with the mean value, Embarked values can be filled with the mode value as it is categorical
data["Age"].fillna(data["Age"].mean(), inplace=True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)

# Convert data types
data["Age"] = data["Age"].astype(int)

# Drop columns: PassengerId doesn't contribute to anything, Ticket has a lot of duplicates and may not correlate to the analysis, 
# Cabin has a lot of missiong values, Name also doesn't contribute to anything
drop_columns = ["PassengerId", "Ticket", "Cabin", "Name"]
data = data.drop(drop_columns, axis=1)

# Combine columns (siblings/spouses and parents/children) into a single column Family
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
data = data.drop(["SibSp", "Parch"], axis=1)

# Transform categorical data into numerical data manually as there are only 2 to 3 values for each column
data['Survived'] = data['Survived'].map( {'Yes': 1, 'No': 0} ).astype(int)
data['Sex'] = data['Sex'].map( {'female': 1, 'male': 0} ).astype(int)
data['Embarked'] = data['Embarked'].map( {'S': 0, 'C': 1, 'Q': 2} ).astype(int)

# Verifications that the data is ready to be treated
print("Verifications that the data is ready to be treated:")
print("Summary Datatypes:\n", data.info(), end = "\n\n")
print("Summary Statistics:\n", data.describe(include = "all"), end = "\n\n")
print("Number of missing values:\n", data.isnull().sum(), end = "\n\n")