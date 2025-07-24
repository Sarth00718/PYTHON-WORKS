'''Write a Python program to print the alphabet pattern 'E' '''
r_str=""
for row in range(0,7):
    for col in range(0,7):
        if(col==1 or ((row==0 or row==6) and (col>1 and col<6))or (row==3 and col>1 and col<5)):
            r_str=r_str="*"
        else:
            r_str=r_str+" "
    r_str=r_str+"\n"
print(r_str)

