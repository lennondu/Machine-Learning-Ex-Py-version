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
X = pd.DataFrame(data['Population'],columns=['Population'])
y = pd.DataFrame(data['Profit'],columns=['Profit'])

m = y.shape[0] #number of training examples

# Plot Data
# Note:You have to complete the code in plotData.py
plotData(X,y)
print "Program paused. Press enter to continue.\n"
raw_input()

## =================== Part 3: Gradient descent ===================
print 'Running Gradient Descent ...\n'

X['Residual']=np.ones(m) #Add a column of ones to x
theta = np.zeros((2,1)) # initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# compute and display initial cost
print 'J = ',computeCost(X,y,theta)

# run gradient descent
theta,J_his = gradientDescent(X,y,theta,alpha,iterations)

# print theta to screen
print "Theta found by gradient descent:"
print "%f %f" % (theta[0],theta[1])

# Plot the linear fit
plt.figure(2)
plt.plot(X['Population'],np.dot(X,theta),'-')
plt.legend(handles=["Traiing data","Linear regression"])

# Predict values for population sizes of 35,000 and 70,000

