import numpy as np


def compute_cost(X, y, theta):
    m = len(y)
    pred_y = np.dot(X, theta)
    diff = pred_y - y
    J = np.sum(diff ** 2) / (2 * m)
    return J


def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    J_history = np.zeros((m, 1))
    for i in range(m):
        diff = np.dot(X, theta) - y
        theta = theta - alpha/m * np.dot(X.transpose(), diff)
        J_history[i] = compute_cost(X, y, theta)
    print(J_history)
    return theta
