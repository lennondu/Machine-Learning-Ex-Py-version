#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from computeCost import computeCost
def gradientDescent(X, y, theta, alpha, num_iters):
    m = y.shape[0]
    J_history = np.zeros((num_iters,1))

    for i in np.arange(num_iters):
        theta = theta - alpha*(1/m)*np.transpose(np.dot(np.transpose(np.dot(X,theta).reshape(m,1)-y.values),X))

        J_history[i] = computeCost(X, y, theta)

    return theta,J_history
