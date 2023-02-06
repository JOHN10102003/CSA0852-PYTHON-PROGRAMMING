x=int(input("X = "))
n=int(input("N = "))
while True:
    print("\n1. Power \n2. Add \n3. Subtract \n4. Multiply \n5. Divide")
    ch=int(input("Enter the choice: "))
    if ch==1:
        c=x**n
        print("Power = ",c)
    elif ch==2:
        c=x+n
        print("Sum = ",c)
    elif ch==3:
        c=x-n
        print("Difference = ",c)
    elif ch==4:
        c=x*n
        print("Product = ",c)
    elif ch==5:
        c=x/n
        print("Division = ",c)
    else:
        print("Enter valid choice from 1 to 5")
        break
