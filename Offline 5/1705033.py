# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:14:30 2019

@author: HP
"""

import math
import numpy as np
from matplotlib import pyplot as plt

def f(x, y):
    return (x + 20 * y) * math.sin(x * y)

def second_RK(a2, stepSize):
    x = []
    y = []
    a1 = 1 - a2
    Yi = 4
    x = np.arange(0, 10, stepSize)
    listSize = 10 / stepSize
    i = 1
    y.append(4)
    if(a2 == 0.5):
        string = "Huen's Method " + str(stepSize) + " Step Size"
    elif(a2 == 1):
        string = "Midpoint Method " + str(stepSize) + " Step Size"
    else:
        string = "Ralston's Method " + str(stepSize) + " Step Size"
    while( i < listSize):
        k1 = f(x[i - 1], y[i - 1])
        if(a2 == 0.5):
            k2 = f(x[i - 1] + stepSize, y[i - 1] + k1 * stepSize)
        elif(a2 == 1):
            k2 = f(x[i - 1] + (1 / 2) * stepSize, y[i - 1] + (1 / 2) * k1 * stepSize)
        else:
            k2 = f(x[i - 1] + (3 / 4) * stepSize, y[i - 1] + (3 / 4) * k1 * stepSize)
        Ynext = Yi + (a1 * k1 + a2 * k2) * stepSize
        y.append(Ynext)
        Yi = Ynext
        i = i + 1
    plt.plot(x, y, label = string)
    plt.legend(loc = 'best')
    plt.xlabel("x")
    plt.ylabel("y")
        
def fourth_RK(stepSize):
    x = []
    y = []
    Yi = 4
    y.append(4)
    x = np.arange(0, 10, stepSize)
    listSize = 10 / stepSize
    i = 1
    string = "4th order RK Method " + str(stepSize) + " Step Size"
    while( i < listSize):
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + (1 / 2) * stepSize, y[i - 1] + (1 / 2) * k1 * stepSize)
        k3 = f(x[i - 1] + (1 / 2) * stepSize, y[i - 1] + (1 / 2) * k2 * stepSize)
        k4 = f(x[i - 1] + stepSize, y[i - 1] + k3 * stepSize)
        Ynext = Yi + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * stepSize
        y.append(Ynext)
        Yi = Ynext
        i = i + 1
    plt.plot(x, y, label = string)
    plt.legend(loc = 'best')
    plt.xlabel("x")
    plt.ylabel("y")

def Euler(stepSize):
    x = []
    y = []
    Yi = 4
    y.append(4)
    x = np.arange(0, 10, stepSize)
    listSize = 10 / stepSize
    i = 1
    string = "Euler Method " + str(stepSize) + " Step Size"
    while( i < listSize):
        k1 = f(x[i - 1], y[i - 1])
        Ynext = Yi + k1 * stepSize
        y.append(Ynext)
        Yi = Ynext
        i = i + 1
    plt.plot(x, y, label = string)
    plt.legend(loc = 'best')
    plt.xlabel("x")
    plt.ylabel("y")
        
plt.figure(figsize = (10, 10))
plt.title("All methods with 0.01 step size")
plt.grid()
Euler(0.01)
fourth_RK(0.01)
second_RK(0.5, 0.01)
second_RK(1, 0.01)
second_RK(2 / 3, 0.01)

plt.figure(figsize = (10, 10))
plt.title("All methods with 0.05 step size")
plt.grid()
Euler(0.05)
fourth_RK(0.05)
second_RK(0.5, 0.05)
second_RK(1, 0.05)
second_RK(2 / 3, 0.05)

plt.figure(figsize = (10, 10))
plt.title("All methods with 0.1 step size")
plt.grid()
Euler(0.1)
fourth_RK(0.1)
second_RK(0.5, 0.1)
second_RK(1, 0.1)
second_RK(2 / 3, 0.1)

plt.figure(figsize = (10, 10))
plt.title("All methods with 0.5 step size")
plt.grid()
Euler(0.5)
fourth_RK(0.5)
second_RK(0.5, 0.5)
second_RK(1, 0.5)
second_RK(2 / 3, 0.5)

plt.figure(figsize = (10, 10))
plt.title("Euler method with four different step size")
plt.grid()
Euler(0.01)
Euler(0.05)
Euler(0.1)
Euler(0.5)

plt.figure(figsize = (10, 10))
plt.title("4th RK method with four different step size")
plt.grid()
fourth_RK(0.01)
fourth_RK(0.05)
fourth_RK(0.1)
fourth_RK(0.5)

plt.figure(figsize = (10, 10))
plt.title("Huen's method with four different step size")
plt.grid()
second_RK(0.5, 0.01)
second_RK(0.5, 0.05)
second_RK(0.5, 0.1)
second_RK(0.5, 0.5)

plt.figure(figsize = (10, 10))
plt.title("Midpoint method with four different step size")
plt.grid()
second_RK(1, 0.01)
second_RK(1, 0.05)
second_RK(1, 0.1)
second_RK(1, 0.5)

plt.figure(figsize = (10, 10))
plt.title("Ralston's method with four different step size")
plt.grid()
second_RK(2 / 3, 0.01)
second_RK(2 / 3, 0.05)
second_RK(2 / 3, 0.1)
second_RK(2 / 3, 0.5)