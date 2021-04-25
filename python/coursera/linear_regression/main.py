import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('../linear_regression/data/ex1data1.txt', header=None)
x_values = data.values[:, 0]
y_values = data.values[:, 1]
m = len(y_values)

plt.plot()
