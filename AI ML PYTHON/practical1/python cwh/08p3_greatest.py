def max(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3
        
m = max(3,5, 234)
print("the value of the maximum is" + str(m))
    