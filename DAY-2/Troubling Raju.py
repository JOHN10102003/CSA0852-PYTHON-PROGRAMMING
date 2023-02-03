def reverse(s): 
         str = "" 
         for i in s: 
                 str = i + str 
         return str 
  
 s=input("Enter the number: ") 
 print("Mirror image: ", end="") 
 print(reverse(s))
