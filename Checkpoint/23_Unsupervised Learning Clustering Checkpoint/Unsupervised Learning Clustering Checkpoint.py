import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import StandardScaler
from sklearn.metrics import silhouette_score

# Load the dataset
data = pd.read_csv('CC GENERAL.csv')

# Drop the categorical 'CUST_ID' column as it's not required for clustering
data_numeric = data.drop('CUST_ID', axis=1)

data_numeric = data_numeric.fillna(data_numeric.mean())

# print("Data head", end = "\n\n")
# print(data_numeric.head(), end = "\n\n")

# print("Data info", end = "\n\n")
# print(data_numeric.info(), end = "\n\n")

# print("Data describtion", end = "\n\n")
# print(data_numeric.describe(), end = "\n\n")

cols = ['BALANCE', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'ONEOFF_PURCHASES_FREQUENCY','PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT']
for col in cols:
    data_numeric[col] = np.log(1 + data_numeric[col])

# --- Applying PCA ---
pca = PCA(n_components=0.95)
X_red = pca.fit_transform(data_numeric)

# Perform hierarchical clustering
linked = linkage(X_red, method='ward')

# Plot the dendrogram
plt.figure(figsize=(12, 6))
dendrogram(linked, orientation='top', truncate_mode='level', p=5)
plt.title('Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()

# Find the optimal k value using the Elbow method
inertia_values = []
cluster_results = {}
k_values = range(1, 10)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(X_red)
    inertia_values.append(kmeans.inertia_)
    cluster_results[k] = kmeans.predict(X_red)

# Plot the Elbow method graph
plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve')
plt.show()

# Calculate silhouette scores for different k values
k_values = range(2, 10)
silhouette_scores = []
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    labels = kmeans.fit_predict(X_red)
    score = silhouette_score(X_red, labels)
    silhouette_scores.append(score)

# Plot the silhouette scores
plt.figure(figsize=(8, 6))
plt.plot(k_values, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for K-means Clustering')
plt.show()

kmeans = KMeans(n_clusters=2, random_state=42, n_init='auto')
kmeans.fit(X_red)

print(f'Silhoutte score of our model is {str(silhouette_score(X_red, kmeans.labels_))}')

for col in cols:
    data_numeric[col] = np.exp(data_numeric[col])

# Get the cluster results for the best k value
best_k = 2
best_clusters = cluster_results[best_k]

# Add the cluster labels to the original dataset
data_numeric['Cluster'] = best_clusters

# Plot the clusters using the first two features
plt.figure(figsize=(8, 6))
sns.scatterplot(x='ONEOFF_PURCHASES', y='PURCHASES', hue='Cluster', data=data_numeric)
plt.xlabel('ONEOFF_PURCHASES')
plt.ylabel('PURCHASES')
plt.title('Distribution of clusters based on One off purchases and total purchases')
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(data=data_numeric, x='CREDIT_LIMIT', y='PURCHASES', hue='Cluster')
plt.title('Distribution of clusters based on Credit limit and total purchases')
plt.show()