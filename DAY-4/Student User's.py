total=int(input("Enter total number of users: "))
if(total==0):
    print("Student user(s) = 0")
elif(total<0):
    print("Invalid input")
else:
    staff=int(input("Enter the number of staff users: "))
    if(total==staff):
        print("All the users are staff members")
    elif(total<staff):
        print("Invalid input")
    else:
        nostaff=(staff/3)
        print("Student user(s) = ",total-staff-nostaff)
