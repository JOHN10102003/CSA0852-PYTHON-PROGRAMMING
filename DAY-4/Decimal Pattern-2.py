b=int(input("Enter the number of rows: "))
for i in range(b):
    a=0.1
    for j in range(i+1):
        print("%.1f"%a, end=" ")
        a+=0.1
    print()
