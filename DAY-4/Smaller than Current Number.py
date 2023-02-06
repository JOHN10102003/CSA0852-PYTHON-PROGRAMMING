def smallerthancurrent(n):
    l=len(n)
    ans=[]
    for i in n:
        count=0
        for j in range(l):
            if (n[j]-i)<0:
                count+=1
        ans.append(count)
    return ans
n=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    n.append(ele)
print(n)
print(smallerthancurrent(n))
