#!/usr/bin/env python
# encoding: utf-8

import numpy as np
def computeCost(X, y, theta):

    m = len(y)
    J = sum((y - np.dot(X,theta))**2)/(2*m)
    return J

