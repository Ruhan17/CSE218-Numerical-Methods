# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:00:05 2019

@author: HP
"""

import numpy as np

def Decompose(a, n):
    for k in range(0, n-1):
        for i in range(k + 1, n):
            if a[k][k] == 0:
                 continue
            factor = a[i][k] / a[k][k]
            a[i][k] = factor
            for j in range(k + 1 , n):
                a[i][j] = a[i][j] - factor * a[k][j]

def Substitute(a, n, b, x):
    for i in range(1, n):
        sum = b[i][0]
        for j in range(0, i):
            sum = sum - a[i][j] * b[j][0]
        b[i][0] = sum
    x[n - 1] = b[n - 1][0] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum = sum + a[i][j] * x[j]
        if a[i][i] == 0:
            continue
        x[i] = (b[i][0] - sum) / a[i][i] 
        
def MatrixGenerator(a, n, l, u, y, b):
    for col in range(0, n - 1):
        for row in range(col + 1, n):
            l[row][col] = a[row][col]
    for i in range(n):
        l[i][i] = 1
        
    for row in range(0, n):
        for col in range(row, n):
            u[row][col] = a[row][col]
            
    for i in range(0, n):
        y[i] = b[i][0]
        
            
def UniqueSolution(u, n):
    count = 0
    for i in range(0,n):
        count = 0
        for j in range(0, n):
            if(u[i][j] == 0.0):
                count = count + 1
        if(count == n):
            print("No unique solution")
            return 0
    return 1

input = open("in1.txt", "r")

n = int(input.readline())

A = list()

#print(n)

for i in range(n):
    row = list()
    for val in input.readline().split():
         row.append(float(val))
        #row.append(value)
    A.append(row)

#print(A)

B = list()

for i in range(n):
    row = list()
    for val in input.readline().split():
         row.append(float(val))
        #row.append(value)
    B.append(row)

#print(B)

l =  [[0 for x in range(n)]  
                for y in range(n)]
#print(l)

u =  [[0 for x in range(n)]  
                for y in range(n)]

y = list()

for i in range(n):
    row = list()
    y.append(row)
    
X = list()

for i in range(n):
    row = list()
    X.append(row)

Decompose(A, n)
#print(A)
Substitute(A, n, B, X)

MatrixGenerator(A, n, l, u, y, B)
f = open("out1.txt", "w")
for i in range(n):
    for j in range(n):
        f.write("%.4f " % l[i][j])
    f.write("\n")
    
#f = open("out1.txt", "w+")
f.write("\n")

for i in range(n):
    for j in range(n):
        f.write("%.4f " % u[i][j])
    f.write("\n")
#print(l)
#print(u)
if UniqueSolution(u, n) == 1:
        f.write("\n")
        for i in range(n):
            f.write("%.4f" % y[i])
            f.write("\n")
        f.write("\n")
        for i in range(n):
            f.write("%.4f" % X[i])
            f.write("\n")
        #print(y)
        #print(X)
else:
    f.write("\n")
    f.write("No unique solution")

f.close()