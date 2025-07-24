a = {1,3,4,5,1}
print(a)   

#syntex of empty set

b = set()
print(type(b))
b.add(4)
b.add(5)
b.add((4,5,6)) #--> can`t add list and dict`
print(b)

s={20,20.0,"20"}
print(len(s)) # --> int and float value consider as same value

print(len(b))
b.remove(5)
print(b)
print(b.pop())
