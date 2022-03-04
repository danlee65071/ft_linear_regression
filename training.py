import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import csv


def fit(X, y, n_iterations=1000, learning_rate=1):
    m = X.shape[0]
    X_intercept = X.copy()
    X_intercept = StandardScaler().fit_transform(X_intercept)
    X_intercept = np.hstack((np.ones((m, 1)), X_intercept))
    thetas = np.zeros((X_intercept.shape[1], 1))
    for it in range(n_iterations):
        gradient = np.zeros(X_intercept.shape[1])
        for i in range(m):
            gradient += (thetas.T @ X_intercept[i] - y[i]) * X_intercept[i]
        tmp_thetas = learning_rate * (1 / m) * gradient
        thetas -= tmp_thetas.reshape(-1, 1)
    with open('thetas.csv', 'a') as thetas_f:
        csv_writer = csv.writer(thetas_f, delimiter=',')
        csv_writer.writerow([thetas[0][0], thetas[1][0], X.mean(), X.std()])
    return thetas


def predict(X, thetas):
    m = X.shape[0]
    X_intercept = X.copy()
    X_intercept = StandardScaler().fit_transform(X_intercept)
    X_intercept = np.hstack((np.ones((m, 1)), X_intercept))
    return X_intercept @ thetas


def score(X, y):
    y_pred = predict(X, fit(X, y))
    ss_res = ((y - y_pred) ** 2).sum()
    ss_tot = ((y - y.mean()) ** 2).sum()
    plt.plot(X, y_pred)
    plt.scatter(X, y)
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('score')
    plt.show()
    return 1 - ss_res / ss_tot


dt = pd.read_csv('data.csv')
print('Describe:\n', dt.describe(), '\n')
print(dt.info())
dt.plot(kind='scatter', x='km', y='price', grid=True, title='data')
plt.show()
dt.hist()
plt.show()
X = dt['km'].values.reshape(-1, 1)
y = dt['price'].values.reshape(-1, 1)
print('\nscore: ', score(X, y))

