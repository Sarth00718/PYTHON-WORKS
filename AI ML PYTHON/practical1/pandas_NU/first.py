import pandas as pd 
import numpy as np

a=pd.Series(['a','b','c'])
print(a)
'''
x=np.array[1,2,3,4,5]
s=pd.Series(x,index=[101,102,103,104,105])
print(s)
'''
data={'a':0.,'b':1,'c':3.}
b=pd.Series(data)
print(b)

data={'a':0.,'b':1,'c':3.}
b=pd.Series(data,index=['b','c','d','a'])
print(b)

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print((s[:3]))
print((s[-3:]))

s=pd.Series([1,2,3,4,5],index=[2,2,2,3,3])
print((s[2]))
print((s[-3:]))

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print((s[['a','c','d']]))

df=pd.DataFrame()
print(df)

data=[1,2,3,4,5]
df=pd.DataFrame(data)
print(df)
'''
data={'Name':['sarth','heet','het','meet'],'Age'=[24,33,52,45]}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
print(df)'''

data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(data,index=['first','second'])
print(df)

d={'one':pd.Series([1,2,3],index={'a','b','c'}),'two':pd.Series([1,2,3,4],index={'a','b','c','d'})}
df=pd.DataFrame(d)
print(df)

'''print((df=[['a']['one','two']]))'''

df={'Name':pd.Series(['sarth','heet','het','meet']),
   'age':pd.Series([1,2,3,4]),
   'Rate':pd.Series([13.23,12.,.23,12.23])}
df=pd.DataFrame(df)
print(df)
df.sum(axis=0)
print(df)
