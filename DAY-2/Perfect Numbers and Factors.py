def factors(x):
    count=0
    print("\n")
    print("The factors of",x,"are: ")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
            count=count+1
            if(count==m):
                break
n=float(input("Enter the value of N: "))
m=float(input("Enter the number of factor M: "))
count=0
a=1;
fact=[]
if(n<=0 or m<=0):
    print("Invalid input")
    exit()
else:
    while count<n:
        sum=0
        for b in range(1,(a//2)+1):
            if a%b==0:
                sum=sum+b
        if sum==a:
            print("\n",a,end='')
            fact.append(a)
            count+=1
        a+=1
for i in fact:
    factors(i)
