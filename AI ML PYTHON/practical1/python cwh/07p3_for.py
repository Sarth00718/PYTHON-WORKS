'''for i in range(8):
    print(i)
'''
'''for i in range(1,8,2):
    print(i)'''

'''
for i in range(10):
    print(i)
else:
    print("this is inside else of for")'''

#break statement

for i in range(10):
    print(i)
    if i==5:
        break #--> output is 1 2 3 4 5
else:
    print("this is inside else of for")


for i in range(10):
    if i==5:
        continue #--> output is 1 2 3 4 5
    print(i)
else:
    print("this is inside else of for")


