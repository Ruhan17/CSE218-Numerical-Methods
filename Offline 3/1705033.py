# -*- coding%f: utf-8c -*-
"""
Created on Sun Jul 21 22:58:36 2019

@author: HP
"""

import numpy as np
from matplotlib import pyplot as plt

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


input = open("data.txt", "r")

len = file_len("data.txt")

#print(len)

x = []
y = []

count = 0
length = 0


while length < len:
    for val in input.readline().split():
        if count % 2 == 0:
            x.append(float(val))
            count = count + 1
        else:
           y.append(float(val))
           count = count + 1
    length = length + 1
      
"""print(x)
print(y)
print(count)
print(length)"""

AvgY = 0

for i in range(length):
    AvgY = AvgY + y[i]
    
#print(AvgY)

AvgY = AvgY / length

#print(AvgY)

St = 0

for i in range(length):
    St = St + (y[i] - AvgY) * (y[i] - AvgY)
    
#print(St)

plt.figure(figsize = (10, 10))
plt.scatter(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("This is the graph consisting of the given points")

n = 2
arr = [[0 for i in range(n)] for j in range(n)]

"""for row in arr:
    print(row)"""

arr[0][0] = length

for i in range(1, n):
    sum = 0
    for k in range(0, length):
         m = 1
         for j in range(0, i):
            m = m * x[k]
         sum = sum + m
    arr[i][0] = sum
    
"""for row in arr:
    print(row)"""
    
row_count = 0

for column in range(1, n):    
    for i in range(column, column + n):
        sum = 0
        for k in range(0, length):
             m = 1
             for j in range(0, i):
                m = m * x[k]
             sum = sum + m
        arr[row_count % n][column] = sum
        row_count = row_count + 1
        
"""for row in arr:
    print(row)""" 

B = [] 

sumY = 0

for i in range(length):
    sumY = sumY + y[i]

B.append(sumY)

for i in range(1, n):
    sum = 0
    for k in range(0, length):
         m = 1
         for j in range(0, i):
            m = m * x[k]
         sum = sum + m * y[k]
    B.append(sum)
    
#print(B)

solution = np.linalg.solve(arr, B )

#print(solution)
print("First Order: ")

for i in range(n):
    print("a%d = " % i , end = '\t')
    print(solution[i])
    
Sr = 0

for i in range(length):
    Sr = Sr + (y[i] - solution[0] - solution[1] * x[i]) * (y[i] - solution[0] - solution[1] * x[i])
    
#print(Sr)

r = ((St - Sr)/St) ** 0.5

print("r =     %f" % r)

X = np.arange(0, 11, 0.1)   
Y = solution[0] + solution[1] * X
plt.plot(X, Y, label = 'First Order Curve')
plt.legend(loc = 'upper left')

    
n = 3
arr = [[0 for i in range(n)] for j in range(n)]

"""for row in arr:
    print(row)"""

arr[0][0] = length

for i in range(1, n):
    sum = 0
    for k in range(0, length):
         m = 1
         for j in range(0, i):
            m = m * x[k]
         sum = sum + m
    arr[i][0] = sum
    
"""for row in arr:
    print(row)"""
    
row_count = 0

for column in range(1, n):    
    for i in range(column, column + n):
        sum = 0
        for k in range(0, length):
             m = 1
             for j in range(0, i):
                m = m * x[k]
             sum = sum + m
        arr[row_count % n][column] = sum
        row_count = row_count + 1
        
"""for row in arr:
    print(row) """

B = [] 

sumY = 0

for i in range(length):
    sumY = sumY + y[i]

B.append(sumY)

for i in range(1, n):
    sum = 0
    for k in range(0, length):
         m = 1
         for j in range(0, i):
            m = m * x[k]
         sum = sum + m * y[k]
    B.append(sum)
    
#print(B)

solution = np.linalg.solve(arr, B )

#print(solution)
print("Second Order: ")

for i in range(n):
    print("a%d = " % i , end = '\t')
    print(solution[i])
    
X = np.arange(0, 11, 0.1)   
Y = solution[0] + solution[1] * X + solution[2] * X * X
plt.plot(X, Y, label = 'Second Order Curve')
plt.legend(loc = 'upper left')

Sr = 0

for i in range(length):
    Sr = Sr + (y[i] - solution[0] - solution[1] * x[i] - solution[2] * x[i] * x[i]) * (y[i] - solution[0] - solution[1] * x[i] - solution[2] * x[i] * x[i])
    
#print(Sr)

r = ((St - Sr)/St) ** 0.5

print("r =     %f" % r)

    
n = 4
arr = [[0 for i in range(n)] for j in range(n)]

"""for row in arr:
    print(row)"""

arr[0][0] = length

for i in range(1, n):
    sum = 0
    for k in range(0, length):
         m = 1
         for j in range(0, i):
            m = m * x[k]
         sum = sum + m
    arr[i][0] = sum
    
"""for row in arr:
    print(row)"""
    
row_count = 0

for column in range(1, n):       
    for i in range(column, column + n):
        sum = 0
        for k in range(0, length):
             m = 1
             for j in range(0, i):
                m = m * x[k]
             sum = sum + m
        arr[row_count % n][column] = sum
        row_count = row_count + 1
        
"""for row in arr:
    print(row)""" 

B = [] 

sumY = 0

for i in range(length):
    sumY = sumY + y[i]

B.append(sumY)

for i in range(1, n):
    sum = 0
    for k in range(0, length):
         m = 1
         for j in range(0, i):
            m = m * x[k]
         sum = sum + m * y[k]
    B.append(sum)
    
#print(B)

solution = np.linalg.solve(arr, B )

#print(solution)
print("Third Order: ")

for i in range(n):
    print("a%d = " % i , end = '\t')
    print(solution[i])
    
Sr = 0

for i in range(length):
    Sr = Sr + (y[i] - solution[0] - solution[1] * x[i] - solution[2] * x[i] * x[i] - solution[3] * x[i] * x[i] * x[i]) * (y[i] - solution[0] - solution[1] * x[i] - solution[2] * x[i] * x[i] - solution[3] * x[i] * x[i] * x[i])
    
#print(Sr)

r = ((St - Sr)/St) ** 0.5

print("r =     %f" % r)
    
X = np.arange(0, 11, 0.1)   
Y = solution[0] + solution[1] * X + solution[2] * X * X + solution[3] * X * X * X
plt.plot(X, Y, label = 'Third Order Curve')
plt.legend(loc = 'upper left')