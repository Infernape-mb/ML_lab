import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("Toyota.csv")
data.head()
data = data.drop('FuelType', axis=1)
plt.subplots()
sns.heatmap(data.corr(), cmap='Blues')
plt.show()
