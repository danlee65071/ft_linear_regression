import numpy as np
import pandas as pd


def fit(X, y, n_iterations=1000, learning_rate=0.1):
    m = X.shape[0]
    X_intercept = X.copy()
    X_intercept = X_intercept.hstack((np.ones((m, 1)), X_intercept))

