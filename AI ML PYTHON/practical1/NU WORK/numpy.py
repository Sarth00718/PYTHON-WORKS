import numpy as np
#1Darray
c = np.array([1,5,3,9,7],"U32")
print(c)
''' change float as U32 '''
print(type(c))
print(len(c))
print(c.dtype)
print(c.shape)

a=np.array(range(6),float)
print(a)
print(a.dtype)
print(a.shape)
print(a[4])
print(a[2:5])
print(a[1:])
print(a[:4])

#2Darray

p=np.array([1,2],[3,4],int)
print(p)
print(p.shape)
print(len(p))

a=np.array(range(6),float)
print(a)
a=a.reshape((3,2))
print(a)
a=a.transpose()
print(a)

b=np.arange(20,26)
print(b)

b=np.arange(1,5).reshape(2,2)
print(b)
p=b.copy()
print(p)
t=b.transpose()
print(t)
f=b.flatten()
print(f)

z1=np.array([1,2],float)
z2=np.array([3,4,5],float)
z3=np.array([6,7],float)

print(z1,z2,z3)
z4=np.concatenate((z1,z2,z3))
print(z4)

z=np.zeros((2,3),dtype=float)
print(z)
z=np.ones((2,3),dtype=float)
print(z)

# arithmatic oprations

#1D
z1=np.array([1,2],float)
z3=np.array([3,4],float)
print(z1,z3)
print(z1+z3)
print(z1-z3)
print(z1*z3)
print(z1/z3)
print(z3/z1)
print(z3//z1)
print(z1**3)
print(z1**z3)

print(np.e)
print(np.pi)

r=np.array([1,2,3,4,3.5],float)
a=np.pi*r**2
print(r)
print(a)

th=np.array([0,1/4,0.5,3/4,1],float)
print(th)
thm=th*np.pi
print(thm)
sn=thm*np.sin(thm)
print(sn)

x=np.arange(1,5)
print(x)
x=10**x
print(x)
y=np.log10(x)
print(y)
y=np.log(x)
print(y)
y=np.exp(x)
print(y)

n=np.array([1,np.pi,np.e,10.5],float)
print(n)
print(np.floor(n))
print(np.ceil(n))
print(np.rint(n))

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

b=np.array([[11,5,14],[2,5,1],[7,3,9]])
print(b)
c=np.sort(b)
print(c)
c=np.sort(b,axis=1) #-->sort the row wise
print(c)
c=np.sort(b,axis=0) #-->sort the col wise
print(c)

c=np.mean(b,axis=1) #-->mean the row wise
print(c)
c=np.mean(b,axis=0) #-->mean the col wise
print(c)

a=np.array([1,2,1,3,2,3,2,4,3,2],float)
print(a)
print(np.unique(a))

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

r=np.random.rand(3)
print(r)
r=np.random.rand(3,2)
print(r)
r=np.random.randiant(5,10)
print(r)
print(np.random.random())
print(r)