import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("Iris.csv", header='infer').values
x = data[:, 1:-1]
y = data[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y)
print("Shapes", x_train.shape, y_train.shape, x_test.shape, y_test.shape)

k = int(input("Enter the number of clusters you want to divide your data into (k): "))
n = int(input("Enter the number of iterations: "))  

per=np.random.permutation(x_train.shape[0])
print(per)

centroid = np.zeros(shape=(k, x_train.shape[1]))
for i in range(k):
    centroid[i, :] = x_train[per[i], :]
print(centroid)

for it in range(n):
    dist = np.zeros(shape=(k, x_train.shape[0]))
    for i in range(k):
        dist[i, :] = np.sqrt(np.sum((x_train - centroid[i, :]) ** 2, axis=1))
    membership = np.argmin(dist, axis=0)
    for i in range(k):
        centroid[i, :] = np.mean(x_train[membership == i, :], axis=0)
print(membership)

print("Centroid after"+str(n)+"iterations:")
print(centroid)

dist = np.zeros(shape=(k, x_test.shape[0]))
for i in range(k):
    dist[i] = np.sqrt(np.sum((x_test - centroid[i]) ** 2, axis=1))
membership = np.argmin(dist, axis=0)
                 
print(y_test.astype(int))
print(membership)