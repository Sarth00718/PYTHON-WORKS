
print("hello world")

a=25+56j
b=23+85j
print(a/b)
print(type(a))
print(type(a*b))

c='''nirma university'''
print(c[:12])

list=['abcd',789,2.2532,'sarth',1+12j]
tinylist=[123,'sarth']
print(list)
print(list[0])
print(list[1:3])
print(list[1:])
print(list+tinylist)
print(list*2)

tuple=('abcd',789,2.2532,'sarth',1+12j)
tinytuple=(123,'sarth')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[1:])
print(tuple+tinytuple)
print(tuple*2)

list[3]=28.99
# tuple(3)=23.233 --> not run it says diff btw list and tuple
print(list,tuple)

dict={}
dict['one']= '''there is the one'''
dict[2]="there is two"
tinydict = {'name':'sarth','code':4586}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

a=input("enter a")
a=int(a)
s=print("enter a",a)

import math
def mul(a,b):
    result =a*b
    return result
if __name__ == '__main__':
    x=mul(1,2)
    print(x)
