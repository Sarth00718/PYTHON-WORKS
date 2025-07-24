n= int(input("n"))
def sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n + sum(n-1)
sum = sum(n)
print(sum)