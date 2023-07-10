import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def k_means(K,X):
    centroids=X[:K]
    print(centroids)
    for _ in range(100):
        labels=np.argmin(np.linalg.norm(X[:,np.newaxis]-centroids,axis=2),axis=1)
        new_centroids=np.array([X[labels==k].mean (axis=0)for k in range(K)])
        if np.all(centroids==new_centroids):
            break;
        centroids=new_centroids
    return labels,centroids

data=pd.read_csv("Iris.csv")
X=data.drop('Species',axis=1).values
labels,centroids=k_means(3,X)
plt.scatter(X[:,0],X[:,1],c=labels)
plt.scatter(centroids[:,0],centroids[:,1],marker='x',color='red',s=200)
plt.xlabel("Sepal Length")
plt.ylabel("sepal width")
plt.title("K-means algorithm for Iris dataset")
plt.show()