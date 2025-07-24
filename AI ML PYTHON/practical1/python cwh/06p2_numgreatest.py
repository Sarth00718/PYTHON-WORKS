n1 = int( input("enter number 1:") )
n2 = int( input("enter number 2:") )
n3 = int( input("enter number 3:") )
n4 = int( input("enter number 4:") )

if(n1>n4):
    f1 = n1
else:
    f1 = n4

if(n2>n3):
    f2 = n2
else:
    f2 = n3

if(f1>f2):
    print(str(f1)+" is greatest")
else:
    print(str(f2)+" is greatest")   