import seaborn as sns
import matplotlib.pyplot as plt


data = [2, 4, 5, 16, 55, 11, 41]

sns.boxplot(data=data, color='red')
plt.title("Box Plot")
plt.show()

sns.histplot(data, bins=5, kde=False, color='cyan') 
plt.title("Histogram")
plt.show()