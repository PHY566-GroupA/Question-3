from numpy import *
import random

# grid size
x=4
y=6

# generating the grid
a=zeros((x,y))

# one-third of the grid to be filled with gas species 'A'
for i in range(0,4):
    for j in range(0,y/2):
        a[i,j]=1.0

# one-third of the grid to be filled with gas species 'B'
for i in range(0,4):
    for j in range(2*y/3,6):
        a[i,j]=2.0

for i in range(0,9999):
    while True:                             # random selection of only occupied sites
        i=random.choice(range(0,x))
        j=random.choice(range(0,y))
        if a[i,j] != 0.0:
            break

    r=random.random()

    if 0.0<=r<=0.25:
        if i<x-1:
            if a[i+1,j] == 0:
                a[i+1,j] = a[i,j]
                a[i,j]= 0
    elif 0.25 < r <= 0.5:
        if i>0:
            if a[i-1,j] == 0:
                a[i-1,j]=a[i,j]
                a[i,j] = 0
    elif 0.5 < r <= 0.75:
        if j<y-1:
            if a[i,j+1]== 0:
                a[i,j+1] = a[i,j]
                a[i,j] = 0
    else:
        if j>0:
            if a[i,j-1] == 0:
                a[i,j-1] = a[i,j]
                a[i,j] = 0

print a
