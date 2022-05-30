# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:40:51 2019

@author: HP
"""

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def checkNegative(arr, columns):
    for i in range(columns - 1):
        if arr[0][i] < 0:
            return 1
    return 0
    
#n = int(input())
#m = int(input())
input = open("in2.txt", "r")

len = file_len("in2.txt")
#print(len)

n = 0

theInts = []
for val in input.readline().split():
    theInts.append(int(val))
    n = n + 1
    
m = 0

#print(theInts)

while m < len - 1:
    for val in input.readline().split():
        theInts.append(float(val))
    m = m + 1

#print(n)
#print(m)

#print(theInts)

rows, columns = (m + 1, n + m + 3)

arr = [[0 for i in range(columns)] for j in range(rows)] 
#print(arr) 
"""for row in arr: 
    print(row)
    
print()"""

arr[0][0] = 1
list_idx = 0

for i in range(n):
    #a = int(input())
    arr[0][i + 1] = -theInts[list_idx]
    list_idx = list_idx + 1

f"""or row in arr: 
    print(row)
    
print()"""

k = 1
l = 2

for i in range(m):
    #print(i)
    for j in range(n):
        #a = float(input())
        arr[k][j + 1] = theInts[list_idx]
        #print(list_idx)
        list_idx = list_idx + 1
   # b = float(input())
    arr[k][columns - 2] = theInts[list_idx]
    list_idx = list_idx + 1
    arr[k][j + l] = 1
    l = l + 1
    k = k + 1
    
for row in range(0, rows):
       for i in range(0, columns):
           print("%.2f" % arr[row][i], end = '\t')
       print()
print()

#count = 0  
while checkNegative(arr, columns) == 1:
    #step 2
    #count = count + 1
    min = 100
    for i in range(columns):
        if(arr[0][i] < min):
            index = i
            min = arr[0][i]
    print("Selected column is %d" % index)
    print()
    
    #step 3
    for i in range(rows):
        if(arr[i][index] == 0):
            arr[i][columns - 1] = 99999999
        else:
            arr[i][columns - 1] = arr[i][columns - 2] / arr[i][index]
            
    for row in range(0, rows):
       for i in range(0, columns):
           print("%.2f" % arr[row][i], end = '\t')
       print()
    print()
        
    #step 4
    for i in range(1, rows):
        if(arr[i][columns - 1] > 0):
            min = arr[i][columns - 1]
            idx = i
            break
        
    for i in range(1, rows):
        if(arr[i][columns - 1] < min and arr[i][columns - 1] > 0):
            min = arr[i][columns - 1]
            idx = i
    
    print("Selected row is %d" % idx)
    print()
    
    #step 5
    a = arr[idx][index]
    
    for i in range(columns):
        arr[idx][i] = arr[idx][i] / a
    
    for row in range(0, rows):
       for i in range(0, columns):
           print("%.2f" % arr[row][i], end = '\t')
       print()
        
    print()
        
    for i in range(rows):
        mul = arr[i][index]
        for j in range(columns):
            if i == idx:
                break
            if(i == 0 and j == columns - 1):
                continue
            arr[i][j] = arr[i][j] - mul * arr[idx][j]
    
    for row in range(0, rows):
       for i in range(0, columns):
           print("%.2f" % arr[row][i], end = '\t')
       print()
    #if count == 3:
        #break
    print()
        
print("result is %.2f" % arr[0][columns - 2])
    