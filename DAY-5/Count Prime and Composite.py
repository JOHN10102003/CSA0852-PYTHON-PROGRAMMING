q=int(input("Enter the length of numbers in list: "))
pcount=0
ccount=0
for i in range (0,q):
    a=int(input("Enter the value: "))
    if a>1:
        for i in range(2,int(a/2)+1):
            if(a%i)==0:
                ccount+=1
                break
        else:
            pcount+=1
    elif a<0:
        print("\nNegative numbers are not allowed in this operation")
    else:
        pcount=0
        ccount=0
print("\n")
print("Prime count: ",pcount)
print("Composite count: ",ccount)
