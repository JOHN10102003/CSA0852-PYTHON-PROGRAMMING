p=int(input("Enter the principal amount: "))
t=int(input("Enter the number of years: "))
while True:
    ch=str(input("Is the customer a senior citizen? (y/n): "))
    if (ch=="y"):
        si=(p*t*(12))/100
        print("Interest: ", si)
        break
    elif (ch=="n"):
        si=(p*t*(10))/100
        print("Interest: ", si)
        break
    else:
        print("Enter valid choice. Select 'y' or 'n'")
        break
