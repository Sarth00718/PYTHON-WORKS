import numpy as np
import statistics as st
import math
#-------------------------------------------------------------------------------------- 
#mean using library

mylist=[]
n=int(input("Enter how many numbers you want"))
for i in range(n):
    num=float(input("Enter the number="+ str(i+1)+":"))
    mylist.append(num)
print(mylist)

myarray=np.array(mylist)
print(myarray)

a=np.mean(myarray)
print("mean",a)

#median using library
b=np.median(myarray)
print("median",b)

#mode using library
c=st.mode(myarray)
print("mode",c)

#std using library
d=np.std(myarray)
print("std",d)

#max min using library
max=np.max(myarray)
min=np.min(myarray)
e=max-min
print("range",e)

#variance using library
p=st.variance(myarray)
print("variance",p)

#---------------------------------------------------------------------------------------

#mean without lib
sum=0
for ele in myarray:
    sum+=ele
    avg=sum/n
print("MEAN = ",avg)

#median without lib
for i in range(n):
    for j in range(i+1,n):
        if myarray[i]>myarray[j]:
            temp = myarray[i]
            myarray[i] = myarray[j]
            myarray[j] = temp
    if n%2==0:
       median=((myarray[n//2]+myarray[n//2+1])//2)
    else:
       median=myarray[n//2]
print("MEDIAN",median)

#varience without lib
sum=0
for ele in myarray:
    sum+=(ele-avg)**2
    var=sum/n
print("VARIANCE",var)

#Standard Deviation without lib
std=np.sqrt(var)
print("STANDERD DEVIATION",std)

#Range without lib
for ele in myarray:
    min=myarray[0]
    max=myarray[-1]
    range=max-min
print("RANGE",range)

#Mode without lib 
dict = {}
for ele in myarray:
    dict[ele] = 0
for ele in myarray:
    dict[ele] = dict[ele] + 1
print(dict)
max1 = 1
mode = []
for key, val in dict.items():
    if val > max1:
        max1 = val
        mode = [key]
    elif val == max1:
        mode.append(key)
if max1 == 1 or not mode:
    print("No mode")
else:
    print("MODE:", mode)
