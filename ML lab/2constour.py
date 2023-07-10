import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Toyota.csv')
dataset.head(5)
x = dataset['Age']
y = dataset['KM']
z = dataset['Price']

# Create a contour plot
plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.colorbar(label='Price')
plt.xlabel('Age')
plt.ylabel('KM')
plt.title('Contour Plot of Price vs. Age and KM')
plt.show()