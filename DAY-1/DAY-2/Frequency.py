def frequency(s): 
     freq=[0]*26 
     n=len(s) 
     for i in range(n): 
         freq[ord(s[i])-ord('a')]+=1 
     for i in range(n): 
         add=freq[ord(s[i])-ord('a')]%26 
         if (ord(s[i])+add<=ord('z')): 
             s[i]=chr(ord(s[i])+add) 
         else: 
             add=(ord(s[i])+add)-(ord('z')) 
             s[i]=chr(ord('a')+add-1) 
     print("".join(s)) 
  
 
 string=input("Enter a string: ") 
 frequency([i for i in string])
