
#print(this)
#print(this.strip())

def rem_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this ="  sarth is a good boy  "
n =rem_and_strip(this,"sarth")
print(n)
