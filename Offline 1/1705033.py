# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:02:39 2019

@author: HP
"""

import numpy as np
from matplotlib import pyplot as plt

x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sum = 0.0
i = 1
X = x
while i <= n:
    if i % 2 == 1:
        sum = sum + x
    else:
        sum = sum - x
    x = (X ** (i + 1)) / (i + 1)
    i = i + 1
    
print(sum)

x = np.arange(1, -1, -0.1)
y = np.log(1 + x)
plt.figure(figsize = (10, 10))
plt.plot(x, y, label = 'ln(1+x)', color = 'navy')
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("ln(1+x)")
plt.title("This is the graph for y = ln(1 + x) function")

y = x
plt.plot(x, y, label = '1 term')
plt.legend()

y = x - (x ** 2) / 2 + (x ** 3) /3
plt.plot(x, y, label = '3 terms')
plt.legend()

y = x - (x ** 2) / 2 + (x ** 3) / 3 - (x ** 4) / 4 + (x ** 5) / 5
plt.plot(x, y, label = '5 terms')
plt.legend()

i = 1
y = 0
while i <= 20:
    if i % 2 == 1:
        y = y + (x ** i) / i
    else:
        y = y - (x ** i) / i
    i = i + 1
plt.plot(x, y, label = '20 terms')
plt.legend()

i = 1
y = 0
while i <= 50:
    if i % 2 == 1:
        y = y + (x ** i) / i
    else:
        y = y - (x ** i) / i
    i = i + 1
plt.plot(x, y, label = '50 terms')
plt.legend()

x = np.arange(2,51,1)
y = list()
previous = 0.5
for i in x:
    if i % 2 == 0:
        current = previous - (0.5 ** i) / i
        if current > previous:
            error = (current - previous) / current
        else:
            error = (previous - current) / current
        error = error * 100
        y.append(error)
        previous = current
    else:
        current = previous + (0.5 ** i) / i
        if current > previous:
            error = (current - previous) / current
        else:
            error = (previous - current) / current
        error = error * 100
        y.append(error)
        previous = current
#print(y)
plt.figure(figsize = (10, 10))
plt.plot(x, y)
plt.scatter(x,y)
#plt.legend()
plt.grid()
plt.xlabel("number of terms taken")
plt.ylabel("relative approx. error(%)")
plt.title("The graph shows relation between number of iterations & relative approx. error")


