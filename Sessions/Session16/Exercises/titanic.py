import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_recall_curve

df = pd.read_csv("train.csv")

# print("Data head", end = "\n\n")
# print(df.head(), end = "\n\n")

# print("Data info", end = "\n\n")
# print(df.info(), end = "\n\n")

# print("Data describtion", end = "\n\n")
# print(df.describe(), end = "\n\n")

Embarked = pd.get_dummies(df.Embarked , prefix='Embarked')
df = df.join(Embarked)
df.drop(['Embarked'], axis=1, inplace=True)

# df.Sex = df.Sex.map({'male':1, 'female':2})

survived_counts = df['Survived'].value_counts().reset_index()
survived_counts.columns = ['Survived', 'Count']
fig = px.pie(survived_counts, values='Count', names=['No', 'Yes'], title='Survived', labels={'Count': 'Count'}, color = ['No', 'Yes'])
fig.update_traces(textposition='inside',  textinfo='percent+label+value')
fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')
fig.show()

fig1 = px.histogram(df, x='Sex', color='Survived', barmode='group', color_discrete_map={0: "red", 1: "blue"})
fig1.update_layout(title='Sex: Survived vs Dead')
fig1.show()

fig2 = px.histogram(df, x='Pclass', color='Survived', barmode='group', title='Pclass: Survived vs Dead', labels={'Pclass': 'Pclass'}, color_discrete_map={0: 'red', 1: 'blue'})
fig2.update_layout(title='PClass: Survived vs Dead')
fig2.show()

# # Calculate the correlation matrix
# correlation_matrix = df.corr()
# print(correlation_matrix)
# # Plot the correlation heatmap
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()

# target_corr = correlation_matrix['Survived']
# print(target_corr)
# print(target_corr.sort_values(ascending=False))

# y = df.Survived.copy()
# X = df.drop(['Survived'], axis=1)

# X.drop(['Cabin'], axis=1, inplace=True) 
# X.drop(['Ticket'], axis=1, inplace=True) 
# X.drop(['Name'], axis=1, inplace=True) 
# X.drop(['PassengerId'], axis=1, inplace=True)

# X.Age.fillna(X.Age.mean(), inplace=True)

# X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, shuffle=True, random_state=1)

# model = LogisticRegression(max_iter=500)
# model.fit(X_train, y_train)

# pred = model.predict(X_train)
# print("\nModel Train Score:\n", accuracy_score(y_train, pred)*100)
# print("\nModel Train Report:\n", pd.DataFrame(classification_report(y_train, pred, output_dict=True)))
# print("\nModel Train Confusion:\n", confusion_matrix(y_train, pred))

# pred = model.predict(X_valid)
# print("\nModel Validation Score:\n", accuracy_score(y_valid, pred)*100)
# print("\nModel Validation Report:\n", pd.DataFrame(classification_report(y_valid, pred, output_dict=True)))
# print("\nModel Validation Confusion:\n", confusion_matrix(y_valid, pred))

# test = pd.read_csv("test.csv")
# Embarked = pd.get_dummies(test.Embarked , prefix='Embarked')
# test = test.join(Embarked)
# test.drop(['Embarked'], axis=1, inplace=True)

# test.Sex = test.Sex.map({'male':0, 'female':1})

# y_test = df.Survived.copy()
# X_test = df.drop(['Survived'], axis=1)

# X_test.drop(['Cabin'], axis=1, inplace=True) 
# X_test.drop(['Ticket'], axis=1, inplace=True) 
# X_test.drop(['Name'], axis=1, inplace=True) 
# X_test.drop(['PassengerId'], axis=1, inplace=True)

# X_test.Age.fillna(X.Age.mean(), inplace=True)

# pred = model.predict(X_test)
# print("\nModel Validation Score:\n", accuracy_score(y_test, pred)*100)
# print("\nModel Validation Report:\n", pd.DataFrame(classification_report(y_test, pred, output_dict=True)))
# print("\nModel Validation Confusion:\n", confusion_matrix(y_test, pred))

# precisions, recalls, thresholds = precision_recall_curve(y_test, pred)
# plt.figure(figsize=(15, 10))
# plt.plot(precisions, recalls)
# plt.xlabel("Precision")
# plt.ylabel("Recall")
# plt.title("PR Curve: precisions/recalls tradeoff")
# plt.show()