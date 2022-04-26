# import required library
import numpy as np
import maplotlib.pyplot as plt
import pandas as pd

# load the dataset and view top five records
dataset = pd.read_csv('Mall_Customer.csv')
x = dataset.iloc[:, [3, 4]].values

# train the Hierarchical Clustering model using dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidian', linkage = 'ward')
y_hc = hc.fit_predict(x)

# visualising the clusters
plt.scatter(x[y_hc == 0, 0], x[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[y_hc == 1, 0], x[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(x[y_hc == 2, 0], x[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(x[y_hc == 3, 0], x[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(x[y_hc == 4, 0], x[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

# https://www.kaggle.com/shwetabh123/mall-customers



# 10 Models for Clustering
    # K-Means
    # Affinity Propagation
    # BIRCH
    # DBSCAN
    # Mini Batch K-Means
    # Mean Shift
    # OPTICS
    # Spectral Clustering
    # Gaussian Mixture Model
    # Agglomerative Clustering




