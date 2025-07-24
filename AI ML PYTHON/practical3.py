import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("train.csv",header='infer')
print(df.head(10))
print(df.describe())
print(df.info())

#mean of the age
meanage=np.mean(df.loc[~df["Age"].isna(),"Age"]) 
print(meanage)
df.loc[df["Age"].isna(),"Age"] = meanage
print(df.info())

#mode of the cabin
mode=(df.loc[~df["Cabin"].isna(),"Cabin"]).mode()[0]
print(mode)
df.loc[df["Cabin"].isna(),"Cabin"] = mode 
print(df.info())

#mode of the embarked
mode2=(df.loc[~df["Embarked"].isna(),"Embarked"]).mode()[0] 
print(mode2)
df.loc[df["Embarked"].isna(),"Embarked"] = mode2
print(df.info())

#age and survived      
meanage0=np.mean(df.loc[~df["Age"].isna() & (df["Survived"]==0),"Age"])
df.loc[df["Age"].isna() & df["Survived"]==0,"Age"]=meanage0
print(meanage0) 

meanage1=np.mean(df.loc[~df["Age"].isna() & (df["Survived"]==1),"Age"]) 
df.loc[df["Age"].isna() & df["Survived"]==1,"Age"]=meanage1
print(meanage1)

#plot different type of the graph using matpotlib applied on the csv file
plt.plot(df['PassengerId'],df['Fare'])
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot')
plt.show()
