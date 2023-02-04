a=int(input("Enter length of array: "))
b=[]
c=[]
for i in range(0,a):
    d=input("Enter the string: ")
    b.append(d)
for i in range(0,a):
    e=len(b[i].split())
    c.append(e)
print("List: ",b)
print("Maximum number of words in a string: ",max(c))
