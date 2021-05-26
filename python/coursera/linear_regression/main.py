import pprint
import pandas as pd
import numpy as np
from functions import compute_cost, gradient_descent
import matplotlib.pyplot as plt


#get data
data = pd.read_csv('../linear_regression/data/ex1data1.txt', header=None)
x_values = data.values[:, 0]
y_values = data.values[:, 1]
m = len(y_values)

# gradient descent setup
X = np.column_stack((np.ones((m,1)), data.values[:, 0])) # add ones column to input for the parameter theta 0
iterations = 1500
alpha = 0.01
theta = np.zeros((2, 1))
y = np.row_stack(data.values[:, 1])


result = gradient_descent(X, y, theta, alpha, iterations)
print(result)
