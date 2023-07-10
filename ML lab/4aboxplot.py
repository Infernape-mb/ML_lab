import numpy as np
import seaborn as sc
import matplotlib.pyplot as plt
import  pandas as pd

data=pd.read_csv('Toyota.csv')
sc.boxplot(data=data[['Age','HP','CC','Weight']])
plt.show()