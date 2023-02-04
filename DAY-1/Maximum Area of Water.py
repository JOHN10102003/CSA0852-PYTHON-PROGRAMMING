
def maxarea(a, len):
    area=0
    for i in range(len):
        for j in range(i+1, len):
            area=max(area, min(a[j], a[i]) * (j-i))
    return area

l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
print("\n")
length=len(l)
print(maxarea(l, length))
