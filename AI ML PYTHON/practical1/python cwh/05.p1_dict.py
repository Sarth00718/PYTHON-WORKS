mydict ={
    "fast": "in a quick manner",
    "sarth": "a begineer coder",
    "marks": [1,2,3],
    "anotherdict": {'sarth':'player'},
    "1": 2
}

print(mydict['sarth'])
print(mydict['anotherdict']['sarth'])
print(mydict['marks'])
mydict['marks']=[45,785]
print(mydict['marks']) 
print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())
updatedict ={
    "heet":'friend'
}
mydict.update(updatedict)
print(mydict)


print(mydict.get("heet"))
print(mydict["heet"]) 
print(mydict.get("heet2")) #--> return none
print(mydict["heet2"]) #--> key error