print("Enter * to exit...") 
 str1="" 
 L=[] 
 l=0 
 u=0 
 n=0 
 for i in range(0,1000): 
     a = input("Enter any character:") 
     L.append(a) 
     if (a=="*"): 
         break 
  
 for i in L: 
     str1+=i 
      
 for i in str1: 
     if (i.islower()): 
         l+=1 
     elif (i.isupper()): 
         u+=1 
     elif (i.isdigit()): 
         n+=1 
  
 print("Total count of lower case :",l) 
 print("Total count of upper case :",u) 
 print("Total count of numbers :",n)
