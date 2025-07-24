# part 1: without sklearn library

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data=pd.read_csv("BostonHousing.csv",header='infer').values
x=data[:,0:-1]
y=data[:,-1]
test_split=eval(input("Enter a number between 0 to 1 to specify the test_split:"))
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=test_split)

dist=np.zeros(shape=x_train.shape[0])
pred=np.zeros(shape=x_test.shape[0])

k=int(input("Enter the number of nearst neighbours to be used:"))

for i in range(x_test.shape[0]):
    dist=np.sqrt(np.sum((x_train-x_test[i])**2,axis=1))
    kminind=np.argpartition(dist,k)[0:k]
    invdist=1/(dist+10e-20)
    denom=sum(invdist[kminind])
    pred[i]=np.dot(invdist[kminind]/denom,y_train[kminind])
print("Pred",pred)

mae = np.mean(abs(pred-y_test))
mse = np.mean((pred-y_test)**2)
rmse = np.sqrt(mse)
mape = np.mean(abs((pred-y_test)/y_test))

print("Without sklearn:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Percentage Error (MAPE):", mape)

# part 2 : using sklearn library

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,mean_absolute_percentage_error

k = int(input("Enter the K neighbors:"))
model = KNeighborsRegressor(n_neighbors=k, weights='distance')
model.fit(x_train, y_train)
pred = model.predict(x_test)

mae = mean_absolute_error(y_test, pred)
mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mean_squared_error(y_test, pred))
mape = mean_absolute_percentage_error(y_test, pred)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Percentage Error (MAPE):", mape)