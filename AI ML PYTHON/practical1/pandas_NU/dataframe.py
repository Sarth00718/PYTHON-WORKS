import numpy as np
import pandas as pd 
'''empdata = { 'empid':[101,102,103,104,105,106] ,
            'ename':['sachin','vinod','Lakhbir','Anil','Devindra','Umaselvi'],
            'Doj':['12-01-2012','15-01-2012','05-09-2007','17-01-2012','05-09-2007','16-01-2012']}

df = pd.DataFrame(empdata) 
print(df)
print(df.loc[0])
print(df.loc[0:2])
print(df.head())
print(df.tail())'''

'''dic = {
'Name' : ['Rishi' , 'Raj' , 'Smit'],
'Age' : [32,35,40] }
df = pd.DataFrame(dic,index = [True , False , True]) 
print(df)
print(df.loc[True]) 
print()
print("Result of the iloc method") 
print(df.iloc[1])'''

dic = {
'id' :[1,2,3,4,5] , 'valuel' :['a','b','c','d', 'e'] ,'value2' : ['A','B','C','D', 'E']
}
dic1 ={
'id' :[6,7,8,9,10] , 'valuel' :['f','g','h','t','e'] ,'value2' : ['f','g','h','D',' E']
}
'''df1 = pd.DataFrame(dic) 
print(df1)
df2 = pd.DataFrame(dic1) 
print(df2)
mearge = {'Datal':df1 , 'Data2':df2} 
df3 = pd.concat(mearge)
print(df3)'''

'''df1 = pd.DataFrame(dic)
df2 = pd.DataFrame(dic1)
df3 = pd.concat([df1,df2],axis=1) 
print(df3)
'''
dic2={'id' :[1,2,3,4,5,6,7,8,9,10] , 'value3' : [12,13,14,15,16,17,18,19,20,21]}
df1 = pd.DataFrame(dic) 
df2 = pd.DataFrame(dic1) 
df3 = pd.concat([df1,df2]) 
print(df3)
print()
df4 = pd.DataFrame(dic2)
print(df4) 
print()
df5 = pd.merge(df3,df4,on='id') 
print(df5)



