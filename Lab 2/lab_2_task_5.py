import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dataset = pd.read_csv('dataset.csv')
plt.scatter(dataset['Feature 1'], dataset['Class'], alpha=0.5)
plt.scatter(dataset['Feature 2'], dataset['Class'], alpha=0.5)
plt.title('Feature VS Class')
plt.xlabel('Feature 1, Feature 2')
plt.ylabel('Class')
plt.show()
