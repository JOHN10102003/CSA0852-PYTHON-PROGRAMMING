l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
m=[]
b=int(input("Enter number of elements: "))
for i in range(0,b):
    ele=int(input("Enter the value: "))
    m.append(ele)
print(m)
c=l+m
c.sort(reverse=False)
print("\n")
print(c)
