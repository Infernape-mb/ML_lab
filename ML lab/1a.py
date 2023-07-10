import numpy as np
import pandas as pd
import plotly.graph_objects as go
data=pd.read_csv('Toyota.csv')
x = data['KM'][:10]
y = data['Age'][:10]
X,Y=np.meshgrid(x,y)
Z = (np.sin(X**2)+np.cos(Y**2))
fig=go.Figure(data=[go.Surface(z=Z)])
fig.show()