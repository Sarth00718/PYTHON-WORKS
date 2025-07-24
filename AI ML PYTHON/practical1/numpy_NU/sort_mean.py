# sort and mean of the arrays
import numpy as np
p=np.array([[11,5,14],[2,5,1],[7,3,9]])
print(p)
q=np.sort(p)
print(q)
q=np.sort(p,axis=1) #-->sort the row wise
print(q)
q=np.sort(p,axis=0) #-->sort the col wise
print(q)

s=np.mean(p,axis=1) #-->mean the row wise
print(s)
s=np.mean(p,axis=0) #-->mean the col wise
print(s)