# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:57:37 2019

@author: HP
"""

from matplotlib import pyplot as plt


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

input = open("input.txt", "r")

len = file_len("input.txt")

count = 0
length = 0
N = 0
x = []
y = []

while length < len:
    for val in input.readline().split():
        if N == 0:
            N = (int(val))
        elif count % 2 == 0:
            x.append(float(val))
            count = count + 1
        else:
           y.append(float(val))
           count = count + 1
    length = length + 1

plt.figure(figsize = (10, 10))
plt.scatter(x, y)
plt.plot(x, y)
plt.title("Numerical Integration")
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")

i = 0
result = 0
count1 = 0
count2 = 0
count3 = 0

while(i < N - 1):
    diff = x[i + 1] - x[i]
    interval = 1
    j = i + 1
    while(j + 1 < N):
        diff1 = x[j + 1] - x[j] 
        if(abs(diff1 - diff) < 0.00001):
            j = j + 1
            interval = interval + 1
        else:
            break    
    if(interval == 1):
        result = result + ((x[i + 1] - x[i]) / 2) * (y[i] + y[i + 1])
        plot_matrix = []
        plot_y = []
        plot_matrix.append(x[i])
        plot_y.append(y[i])
        plot_matrix.append(x[i + 1])
        plot_y.append(y[i + 1])
        count3 = count3 + 1
        if(count3 == 1):
            plt.fill_between(plot_matrix, plot_y, color = 'green', label = "Trapezoid")
            plt.legend(loc = 'best')
        else:
            plt.fill_between(plot_matrix, plot_y, color = 'green')
        
    elif(interval % 3 == 0):
        for k in range(i, j, 3):
            plot_matrix = []
            plot_y = []
            result = result + ((x[k + 3] - x[k]) / 8) * (y[k] + 3 * y[k + 1] + 3 * y[k + 2] + y[k + 3])
            plot_matrix.append(x[k])
            plot_y.append(y[k])
            plot_matrix.append(x[k + 1])
            plot_y.append(y[k + 1])
            plot_matrix.append(x[k + 2])
            plot_y.append(y[k + 2])
            plot_matrix.append(x[k + 3])
            plot_y.append(y[k + 3])
            if(count1 == 0):
                plt.fill_between(plot_matrix, plot_y, color = 'blue', label = "3/8 rule")
                plt.legend(loc = 'best')
            else:
                plt.fill_between(plot_matrix, plot_y, color = 'blue')
            count1 = count1 + 3
    elif(interval % 3 == 2):
        l = j - 2
        plot_matrix = []
        plot_y = []
        result = result + ((x[l + 2] - x[l]) / 6) * (y[l] + 4 * y[l + 1] + y[l + 2])
        plot_matrix.append(x[l])
        plot_y.append(y[l])
        plot_matrix.append(x[l + 1])
        plot_y.append(y[l + 1])
        plot_matrix.append(x[l + 2])
        plot_y.append(y[l + 2])
        if(count2 == 0):
            plt.fill_between(plot_matrix, plot_y, color = 'red', label = "1/3 rule")
            plt.legend(loc = 'best')
        else:
            plt.fill_between(plot_matrix, plot_y, color = 'red')
        count2 = count2 + 2
        for k in range(i, j - 2, 3):
            plot_matrix = []
            plot_y = []
            result = result + ((x[k + 3] - x[k]) / 8) * (y[k] + 3 * y[k + 1] + 3 * y[k + 2] + y[k + 3])
            plot_matrix.append(x[k])
            plot_y.append(y[k])
            plot_matrix.append(x[k + 1])
            plot_y.append(y[k + 1])
            plot_matrix.append(x[k + 2])
            plot_y.append(y[k + 2])
            plot_matrix.append(x[k + 3])
            plot_y.append(y[k + 3])
            if(count1 == 0):
                plt.fill_between(plot_matrix, plot_y, color = 'blue', label = "3/8 rule")
                plt.legend(loc = 'best')
            else:
                plt.fill_between(plot_matrix, plot_y, color = 'blue')
            count1 = count1 + 3
    elif(interval % 3 == 1):
        l = j - 2
        plot_matrix = []
        plot_y = []
        result = result + ((x[l + 2] - x[l]) / 6) * (y[l] + 4 * y[l + 1] + y[l + 2])
        plot_matrix.append(x[l])
        plot_y.append(y[l])
        plot_matrix.append(x[l + 1])
        plot_y.append(y[l + 1])
        plot_matrix.append(x[l + 2])
        plot_y.append(y[l + 2])
        if(count2 == 0):
            plt.fill_between(plot_matrix, plot_y, color = 'red', label = "1/3 rule")
            plt.legend(loc = 'best')
        else:
            plt.fill_between(plot_matrix, plot_y, color = 'red')
        count2 = count2 + 2
        l = j - 4
        plot_matrix = []
        plot_y = []
        result = result + ((x[l + 2] - x[l]) / 6) * (y[l] + 4 * y[l + 1] + y[l + 2])
        plot_matrix.append(x[l])
        plot_y.append(y[l])
        plot_matrix.append(x[l + 1])
        plot_y.append(y[l + 1])
        plot_matrix.append(x[l + 2])
        plot_y.append(y[l + 2])
        if(count2 == 0):
            plt.fill_between(plot_matrix, plot_y, color = 'red', label = "1/3 rule")
            plt.legend(loc = 'best')
        else:
            plt.fill_between(plot_matrix, plot_y, color = 'red')
        count2 = count2 + 2
        for k in range(i, j - 4, 3):
            plot_matrix = []
            plot_y = []
            result = result + ((x[k + 3] - x[k]) / 8) * (y[k] + 3 * y[k + 1] + 3 * y[k + 2] + y[k + 3])
            plot_matrix.append(x[k])
            plot_y.append(y[k])
            plot_matrix.append(x[k + 1])
            plot_y.append(y[k + 1])
            plot_matrix.append(x[k + 2])
            plot_y.append(y[k + 2])
            plot_matrix.append(x[k + 3])
            plot_y.append(y[k + 3])
            if(count1 == 0):
                plt.fill_between(plot_matrix, plot_y, color = 'blue', label = "3/8 rule")
                plt.legend(loc = 'best')
            else:
                plt.fill_between(plot_matrix, plot_y, color = 'blue')
            count1 = count1 + 3
    i = j
        
print("Trapezoid: %d intervals" % count3)
print("1/3: %d intervals" % count2)
print("3/8: %d intervals" % count1)
print("Integration value: %f" % result)