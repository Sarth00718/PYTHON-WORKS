import pandas as pd
import time
import numpy as np

mat=pd.read_csv("11citytsp.csv",header=None).values.astype(float)
print(mat)
sc=int(input("Enter the starting city "))
tl=0 
bst = [sc]
start=time.process_time()
mat[mat==0]=np.inf
print(mat)
mgcopy=mat.copy()

for i in range(mat.shape[0]-1):
    if i==0:
        tl+=min(mat[sc,:])
        nbi=np.argmin(mat[sc,:])
        bst.append(nbi)
        mat[:,sc]=np.inf
        mat[:,nbi]=np.inf
    else:
        tl+=min(mat[nbi,:])
        nbi=np.argmin(mat[nbi,:])
        mat[:,bst]=np.inf
        bst.append(nbi)

tl+=mgcopy[nbi,sc]
end=time.process_time()
taken_time=(end-start)*1000
print("tour length",tl) 
print("best tour ",bst)
print("time taken",taken_time)