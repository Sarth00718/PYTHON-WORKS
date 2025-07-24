# oprators btw 2 arrays
import numpy as np

t=np.array([1,2,1,3,2,3,2,4,3,2],float)
print(t)
print(np.unique(t))

a=np.array([1,3,0.5],float)
b=np.array([0,3,2],float)
print(a,b)
print(a<b)
print(a>b)
print(a==b)
c=a<=b
print(c)
print(any(c))
print(all(c))