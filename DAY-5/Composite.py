a=int(input("Enter the start range: "))
b=int(input("Enter the end range: "))
count=0
for number in range(a,b+1):
    count = 0
    for divider in range(2, number//2+1):
        if number%divider == 0:
            count+=1
    if count >= 1:
        print(number)
