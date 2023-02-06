l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
freq=[None]*len(l)
visited=-1
for i in range(0, len(l)):
    count=1
    for j in range(i+1, len(l)):
        if(l[i]==l[j]):
            count+=1
            freq[j]=visited
    if(freq[i]!=visited):
        freq[i]=count

print("---------------------")   
print(" Element | Frequency")    
print("---------------------")    
for i in range(0, len(freq)):    
    if(freq[i] != visited):    
        print("    " + str(l[i]) + "    |    " + str(freq[i]));    
print("---------------------")
