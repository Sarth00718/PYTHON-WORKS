import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data=pd.read_csv("Iris.csv",header='infer').values
x=data[:,1:-1]
y=data[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y)
print("Shapes",x_train.shape,y_train.shape,x_test.shape,y_test.shape)

# without  skleaarn library

dist=np.zeros(shape=x_train.shape[0])
pred=np.zeros(shape=x_test.shape[0])
classvotes=np.zeros(shape=np.unique(y_train).shape[0])

k=int(input("Enter the number of nearst neighbours to be used:"))

for i in range(x_test.shape[0]):
    dist=np.sqrt(np.sum((x_train-x_test[i])**2,axis=1))
    kminind=np.argpartition(dist,k)[0:k]
    invdist=1/(dist+10e-20)
    denom=sum(invdist[kminind])
    for j in range(k):
        classvotes[int(y_train[kminind[j]])]+=invdist[kminind[j]]
    classvotes/=denom
    pred[i]=np.argmax(classvotes)
print("Prediction",pred)

accuracy = np.mean(pred == y_test)
print("Accuracy",accuracy)

TP = np.sum((pred == y_test) & (pred == 1))
FP = np.sum((pred == 1) & (pred != y_test))
FN = np.sum((pred != 1) & (pred != y_test))

precision = TP / (TP + FP +10e-20)
print("Precision:", precision)

recall = TP / (TP + FN +10e-20)
print("Recall:", recall)

f1_score = 2 * (precision * recall) / (precision + recall +10e-20)
print("F1-score:", f1_score)

#using sklearn library

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, recall_score, f1_score ,precision_score

k = int(input("Enter the K neighbors: "))
model = KNeighborsClassifier(n_neighbors=k, weights="distance")
model.fit(x_train, y_train)
y_predict = model.predict(x_test)

print(y_predict)

accuracy = accuracy_score(y_test, y_predict)
print("Accuracy:", accuracy)

precision = precision_score(y_test, y_predict, average='weighted')
print("Precision:", precision)

recall = recall_score(y_test, y_predict, average='weighted')
print("Recall:", recall)

f1 = f1_score(y_test, y_predict, average='weighted')
print("F1 Score:", f1)

report = classification_report(y_test, y_predict)
print("Classification Report:\n", report)
