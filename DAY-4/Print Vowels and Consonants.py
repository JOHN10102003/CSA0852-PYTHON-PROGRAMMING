string = input("Enter the string: ")
print("\n")
print("Vowels: ")
for ch in string:
   if ch in "AEIOUaeiou":
      print(ch, end=' ')

print("\nConsonants: ")
for ch in string:
   if ch not in "AEIOUaeiou ":
      print(ch, end=' ')
