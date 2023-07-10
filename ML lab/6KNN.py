import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
import pandas as pd

def euclidean_distance(x1,x2):
    distance=np.sqrt(np.sum((x1-x2)**2))
    return distance

class knn:
    def __init__(self,k=3):
        self.k=k
    def fit(self,X,y):
        self.X_train=X
        self.Y_train=y
    def predict(self,X):
        predictions=[self._predict(i)for i in X]
        return predictions
    def _predict(self,x):
        distance=[euclidean_distance(x,i)for i in self.X_train]
        k_indices=np.argsort(distance)[:self.k]
        labels=[self.Y_train[i] for i in k_indices]
        majority=Counter(labels).most_common()
        return majority[0][0]

df=pd.read_csv('glass.csv')

X=df.drop('Type',axis=1).values
Y=df['Type'].values
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=1234)
obj=knn(k=3)
obj.fit(X_train,Y_train)
output=obj.predict(X_test)
accuracy=(np.sum(output==Y_test))/len(Y_test)*100
print(f"Accuracy is {accuracy}")