a=str(input("Enter a string: "))
count=0
for i in a:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        count+=1
print("Number of vowels: ",count)
