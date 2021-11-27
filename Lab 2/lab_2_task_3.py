import pandas as pn
import numpy as np

randomList=pn.DataFrame(np.random.randint(100,size=10))
print(f"List : {randomList}\n Index of : \nSmallest: {randomList.idxmin()}\nLargest: {randomList.idxmax()}")

