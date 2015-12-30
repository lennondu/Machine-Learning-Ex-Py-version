#!/usr/bin/env python
# encoding: utf-8

# Machine Learning Online Class - Exercise 1: Linear Regression

#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the
#  linear exercies. You will need to complete the following functions
#  in this exerice:
#
#    warmUpExercise.py
#    plotData.py
#    gradientDescent.py
#    computeCost.py
#    gradientDescentMulti.py
#    computeCostMulti.py
#    featureNormalize.py
#    normalEqn.py
#
#  For this exercies, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
#

## import package
import sys
## add the current path to the import path
sys.path.append('..')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from warmUpExercise import warmUpExercise
from plotData import plotData
from computeCost import computeCost
from gradientDescent import gradientDescent
## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.py
print "Running warmUpExercise ...\n"
print "5x5 Identity Matrix:\n"
A = warmUpExercise()
print "A=\n",A
print "Program paused. Press enter to continue.\n"
raw_input()

## ======================= Part 2: Plotting =======================
print "Plotting Data ...\n"
data = pd.read_csv('ex1data1.txt',names=['Population','Profit'])
X = data.values[:,0]
y = data.vales[:,1]
m = len(y) #number of training examples

# Plot Data
# Note:You have to complete the code in plotData.py
plotData(X,y)
print "Program paused. Press enter to continue.\n"
raw_input()

## =================== Part 3: Gradient descent ===================
print 'Running Gradient Descent ...\n'

X = np.c_[np.ones(m),X] #Add a column of ones to x
theta = np.zeros((2,1)) # initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# compute and display initial cost
computeCost(X,y,theta)

# run gradient descent
theta = gradientDescent(X,y,theta,alpha,iterations)

# print theta to screen
print "Theta found by gradient descent:"
print "%f %f" % (theta[0],theta[1])

# Plot the linear fit
plt.plot(X[:,1],np.dot(X,theta),'-')
plt.legend("Traiing data","Linear regression")

