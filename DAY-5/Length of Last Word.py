def lastword(a):
    l=0
    x=a.strip()
    for i in range(len(x)):
        if x[i]==" ":
            l=0
        else:
            l+=1
    return l

a=input("Enter the string: ")
print("Length of last word is: ",lastword(a))
