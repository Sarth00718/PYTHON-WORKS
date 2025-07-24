import pandas as pd
mat=pd.read_csv("6citytsp.csv",header=None).values
print(mat)
print(mat.dtype)

#part 1 starting only the first position
from itertools import permutations
citynames=list(range(mat.shape[0]))
per=permutations(citynames)
per=list(per)
print(per)

import numpy as np
import time
st=time.process_time()
besttourlength=np.inf

for tour in per:
    tourlength = 0
    for i in range(len(tour)-1):
        tourlength+=mat[tour[i],tour[i+1]]
    tourlength+=mat[tour[i+1],tour[0]]

    if besttourlength>tourlength:
        besttourlength=tourlength
        besttour=tour
       
et=time.process_time()
time_taken_ms=(et-st)*1000
print(besttour)
print(besttourlength)
print(time_taken_ms)

#part 2  starting with any position
citynames=list(range(mat.shape[0]))
print(citynames)

n=int(input("Enter the start city from 0 to "))

import numpy as np
import time

st = time.process_time()
besttourlength = np.inf
for tour in per:
    tour[0]==n
    tourlength = 0
    for i in range(len(tour)-1):
        tourlength+=mat[tour[i],tour[i+1]]
    tourlength+=mat[tour[i+1],tour[0]]
        
    if besttourlength > tourlength:
        besttourlength=tourlength
        besttour=tour
    
et=time.process_time()
time_taken_ms=(et-st)*1000
print(besttour)
print(besttourlength)
print(time_taken_ms)