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
import warmUpExercise
## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.py
print "Running warmUpExercise ...\n"
print "5x5 Identity Matrix:\n"
A = warmUpExercise.warmUpExercise()
print "A=\n",A
print "Program paused. Press enter to continue.\n"
raw_input()

## ======================= Part 2: Plotting =======================
print "Plotting Data ...\n"
data = pd.read_csv('ex1data1.txt',header=None)
print data.columns

