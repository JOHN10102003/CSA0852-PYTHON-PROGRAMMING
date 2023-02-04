def sumsquare(l):
   odd=0
   even=0
   for i in l:
       if i%2==0:
           even = even + i**2
       else:
           odd = odd + i**2
   l=[odd,even]
   return(l)
l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
print(sumsquare(l))
