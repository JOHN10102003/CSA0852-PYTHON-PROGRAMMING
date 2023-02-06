a=int(input("Enter the employee salary: "))
if(a<10000):
    b=input("Enter the grade of the employee: ")
    c=a*(2/100)
    total=a+c
    print("\n")
    print("Salary: ",a)
    print("Bonus: ",c)
    print("Total to be paid: ",total)
    exit()
b=input("Enter the grade of the employee: ")
if b=='A':
    c=a*(5/100)
    total=a+c
    print("\n")
    print("Salary: ",a)
    print("Bonus: ",c)
    print("Total to be paid: ",total)
elif b=='B':
    c=a*(10/100)
    total=a+c
    print("\n")
    print("Salary: ",a)
    print("Bonus: ",c)
    print("Total to be paid: ",total)
else:
    print("Invalid grade. Choose A or B")
