def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str

#main
s=input("Enter a string/number: ")
if reverse(s)==s:
    print(True)
else:
    print(False)
