# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:44:54 2019

@author: HP
"""

import numpy as np
from matplotlib import pyplot as plt

def function(x):
    return ((x / (1 - x)) * ((6 / (2 + x)) ** 0.5)) - 0.05

def secant(function, x0, x1, n, e):
    for i in range(1, n+1):
        error = abs(x1 - x0)
        #print(error)
        if error < e:
            return x1, i, error
        if (function(x1) - function(x0) == 0):
            error = 0.0
            return x1, i, error
        x_temp = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
        x0 = x1
        x1 = x_temp
        #print(i)
    if i == n:
        print("The estimated error not under given error")
        return None, None, None
 
def false_position(function, xl, xu, n, e):
    while (function (xl) * function (xu)) >= 0:
        print("Give the value of xl &  xu again: ")
        xl = float(input("xl: "))
        xu = float(input("xu: "))
    for i in range(1, n + 1):
        xr = xu - function(xu) * (xl - xu) / (function(xl) - function(xu))
        if not (i == 1 or xr == 0):
            error = abs((xr - xr0) / xr)
            if error < e:
                return xr, i, error
        Test = function(xl) * function(xr)
        if Test == 0:
            error = 0.0
            return xr, i, error
        elif Test < 0:
            xu = xr
            xr0 = xr
        else:
            xl = xr
            xr0 = xr
            
    if i == n:
        print("The estimated error not under given error")
        return None, None, None

x = np.arange(0, 1, 0.001)
y = function(x) 
plt.figure(figsize = (10, 10))
plt.plot(x, y)
plt.grid()

idx = np.argwhere(np.diff(np.sign(y - 0))).flatten()
print('Estimation from graph: ', x[idx])

lower_bound = float(input("Lower bound: "))
upper_bound = float(input("Upper bound: "))
max_itr = int(input("Maximum Iteration: "))
print("\n")

solution, iteration, error = secant(function, lower_bound, upper_bound, max_itr, 0.005)
print("Solution by secant method: %f" % solution)
print("Iteration by secant method: %d" % iteration)
print("Error by secant method: %f" % error)

solution, iteration, error = false_position(function, lower_bound, upper_bound, max_itr, 0.005)
print("Solution by false position method: %f" % solution)
print("Iteration by false position method: %d" % iteration)
print("Error by false position method: %f" % error)



