import numpy as np
# some oprations in log functions,radious,thita
print(np.e)
print(np.pi)

j=np.array([1,2,3,4,3.5],float)
A=np.pi*j**2
print(j)
print(A)

th=np.array([0,1/4,0.5,3/4,1],float)
print(th)
thm=th*np.pi
print(thm)
sn=thm*np.sin(thm)
print(sn)

k=np.arange(1,5)
print(k)
k=10**k
print(k)
l=np.log10(k)
print(l)
m=np.log(k)
print(m)
n=np.exp(k)
print(n)

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
