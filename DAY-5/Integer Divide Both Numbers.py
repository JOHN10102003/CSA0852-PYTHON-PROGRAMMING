a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
count=0
for i in range(1,min(a,b)+1):
    if a%1==b%i==0:
        count+=1
print(count)
