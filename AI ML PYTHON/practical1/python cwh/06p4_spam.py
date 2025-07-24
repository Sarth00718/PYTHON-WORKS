text = input("enter the text")

if("make a lot of money"):
    spam= True
elif("buy now" in  text):
    spam=True
elif("click this" in  text):
    spam=True
elif("subscribe this" in  text):
    spam=True
else:
    spam=False

if(spam):
    print("this text is spam ")
else:
    print("the text is not spam")