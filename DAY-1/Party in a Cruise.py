E=[]
L=[]
T = int(input("Enter value of T: "))
for i in range(T):
    e=int(input("Enter the ENTRY list: "))
    E.append(e)
print(E)
print("\n")
for i in range(T):
    l=int(input("Enter the LEAVING list: "))
    L.append(l)
print(L)
print("\n")
Sum=0
Max=0
for i in range(T):
    Sum+=E[i]-L[i]
    Max=max(Sum,Max)
print("Maximum no. of guests present on cruise: ", Max)
