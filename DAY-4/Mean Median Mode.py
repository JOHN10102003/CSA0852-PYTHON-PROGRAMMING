l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
mean=sum(l)/a
l.sort()
if a%2==0:
    m1=l[a//2]
    m2=l[(a//2)-1]
    median=(m1+m2)/2
else:
    median=l[a//2]

def mode(l):
    count={}
    for i in l:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return [key for key in count.keys() if count[key]==max(count.values())]

print("\n")
print("Mean: ",mean)
print("Median: ",median)
print("Mode: ", mode(l))
