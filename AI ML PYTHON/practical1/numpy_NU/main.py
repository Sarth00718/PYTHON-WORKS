import numpy as np

# some func apply on the 1 D array
o=np.array([1,np.pi,np.e,10.5],float)
print(o)
print(np.floor(o))
print(np.ceil(o))
print(np.rint(o))

v=np.array([1,4,9,25],float)
print(v)
print(np.sqrt(v))
print(np.sum(v))
print(np.prod(v))
print(np.mean(v))
print(np.std(v))
print(np.var(v))
print(np.max(v))
print(np.min(v))
print(np.argmax(v))
print(np.argmin(v))

# sort and mean of the arrays
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

# oprators btw 2 arrays
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

d=np.array([10,np.NaN,np.Inf,np.e,np.pi],float)
print(d)
print(np.isnan(d))
print(np.isinfinite(d))

#random function
r=np.random.rand(3)
print(r)
r=np.random.rand(3,2)
print(r)
r=np.random.randiant(5,10)
print(r)
print(np.random.random())
print(r)