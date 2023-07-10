import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter

def manhatten(x1,x2):
    distance=np.sum(np.abs(x1-x2))
    return distance
class Knn:
    def __init__(self,k=5):
        self.k=k
    def fit(self,X,y):
        self.X_train=X
        self.Y_train=y
    def predict(self,X):
        predictions=[self._predict(i) for i in X]
        return predictions
    def _predict(self,x):
        distance=[manhatten(x,i)for i in self.X_train]
        k_indices=np.argsort(distance)[:self.k]
        labels=[self.Y_train[i]for i in k_indices]
        majority=Counter(labels).most_common()
        return majority[0][0]
fruits=pd.read_csv('fruit.csv')
X=fruits.drop('fruit_label',axis=1).values
Y=fruits['fruit_label'].values
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
obj1=Knn(k=5)
obj1.fit(X_train,Y_train)
predictions=obj1.predict(X_test)
accuracy=(np.sum(predictions==Y_test))/len(Y_test)
print(f"Accuracy of the algorithm is {accuracy}")