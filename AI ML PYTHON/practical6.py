# Without help of the library 

import pandas as pd
import numpy as np
import math
data=pd.read_csv("BostonHousing.csv",header='infer').values
X=data[:,0:-1]
Y=data[:,:-1]

nrows=data.shape[0]
print(nrows)

testsplit=float(input("Enter a number between 0 to 1 to specify how much data is required as test data k : "))

nrows_train=math.floor((1-testsplit)*nrows)
allindices=np.random.permutation(nrows)

X_train=X[allindices[0:nrows_train],:]
Y_train=Y[allindices[0:nrows_train]]
X_test=X[allindices[nrows_train:],:]
Y_test=X[allindices[nrows_train:]]

print("shapes:",X_train.shape,Y_train.shape,X_test.shape,Y_test.shape)
print("Union : " , len(set(allindices[0:nrows_train]).union(allindices[nrows_train:])))
print("Intersection : " , len(set(allindices[0:nrows_train]).intersection(allindices[nrows_train:])))

# With help of the library

import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split  #The library is used for help

data = pd.read_csv("BostonHousing.csv" , header='infer').values

x = data[:,0:-1]
y = data[:,:-1]

nrows = data.shape[0]
print("Total Rows:",nrows)

test_split = eval(input("Enter a number between 0 and 1 to specify the test spilt:"))

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = test_split)
print("shapes:", x_train.shape , y_train.shape , x_test.shape , y_test.shape )
