import numpy as np
d=np.array([10,np.NaN,np.Inf,np.e,np.pi],float)
print(d)
print(np.isnan(d))
print(np.isfinite(d))

#random function
r=np.random.rand(3)
print(r)
r=np.random.rand(3,2)
print(r)
r=np.random.randint(5,10)
print(r)
print(np.random.random())
print(r)