import numpy as np
import pandas as pd

'''arr=np.array(['a','b','c','d']) 
s=pd.Series(arr, index=['first','second', 'third', 'fourth']) 
print(s)'''

'''s = pd.Series(50 , index=[0,1,2,3,4])
print(s)'''

'''d: {'name' : 'Hardik' , 'Iplteam' : 'MI' , 'Runs' : 1500}
s = pd.Series(d)
print(s)
'''

'''s = pd.Series([1,2,3,4,5])
print('To Multiply all values in a series by 2')
print('---------------------------------------------------' )
print(s*2)
print('To find the square of all the values in a series') 
print('----------------------------------------------------')
print(s**2)
print('To print all the values in a series that are greter than 2') 
print(s[s>2])'''

'''s1= pd.Series([1,2,3,4,5], index =['a','b','c','d','e'])
s2=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s3 = pd.Series([5,14,23,32], index =['a','b','c','d']) 
print("To add series1 8 series2")
print ('--------------------------------------------------------------')
print(s1+s2)
print('To add	the series2 &* series3') 
print('---------------------------------------------------------------')
print(s2+s3)
print('To add series2 & series3 and filled Non Matching Index with 0') 
print('----------------------------------------------------------------')
print(s2.add(s3,fill_value=0))'''

'''#usind head function
arr= np.array([10,15,18,22,55,77,42,48,97])
s=pd.Series(arr)
print(s.head())
print(s.head(3))
'''
# using tail function

'''arr = np.array([10,15,18,22,55,77,42,48,97])
s = pd.Series(arr) 
print(s.tail())
print(s.tail(4))'''

arr = np.array([10,15,18,22,55,77]) 
s=pd.Series(arr)
print(s) 
print(s.iloc[:2])
print(s.iloc[3:4])
s.iloc[2:3]



