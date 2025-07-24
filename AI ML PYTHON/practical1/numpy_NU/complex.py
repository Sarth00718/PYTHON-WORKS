import numpy as np

# opration on the complex numbers
z_1=np.array([1,2],float)
z_2=np.array([3,4,5],float)
z_3=np.array([6,7],float)

print(z_1,z_2,z_3)
z_4=np.concatenate((z_1,z_2,z_3))
print(z_4)

z=np.zeros((2,3),dtype=float)
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