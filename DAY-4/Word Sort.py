a=[]
b=[]
n=int(input("Enter the number of elements in list: "))
print("Enter the elements: ")
for i in range(n):
    x=input()
    b=x
    a.append(b)
choice=input("Order by? (A/D): ")
if choice=='A':
    a.sort()
    print("Ascending order: ",a)
elif choice=='D':
    a.sort(reverse=True)
    print("Descending order: ",a)
else:
    print("Wrong choice")
