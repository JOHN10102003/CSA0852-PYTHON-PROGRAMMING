print("Enter -1 to exit...")
L=[]
sum_neg = 0
c_neg = 0
sum_pos = 0
c_pos = 0
for i in range(0,1000):
    a = int(input("Enter the number:"))
    if (a==-1):
        break
    else:
        L.append(a)

for i in L:
    if (i<0):
        sum_neg+=i
        c_neg+=1
    elif (i>0):
        sum_pos+=i
        c_pos+=1

print("The average of negative numbers is :",sum_neg/c_neg)
print("The average of positive numbers is :",sum_pos/c_pos)
