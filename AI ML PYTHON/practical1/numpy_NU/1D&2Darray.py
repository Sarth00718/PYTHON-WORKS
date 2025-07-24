import numpy as np
'''
#1Darray

a=np.array([1,5,3,9,7],"U32")
print(a)
 #change float as U32 
print(type(a))
print(len(a))
print(a.dtype)
print(a.shape)

b=np.array(range(6),float)
print(b)
print(b.dtype)
print(b.shape)
print(b[4])
print(b[2:5])
print(b[1:])
print(b[:4])
'''
#2Darray

c=np.array(([1,2],[3,4]),int)
print(c)
print(c.shape)
print(len(c))

d=np.array(range(6),float)
print(d)
d=d.reshape((3,2))
print(d)
d=d.transpose()
print(d)

e=np.arange(20,26)
print(e)

f=np.arange(1,5).reshape(2,2)
print(f)
g=f.copy()
print(g)
h=g.transpose()
print(h)
i=h.flatten()
print(i)