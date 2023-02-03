def position(str1, str2): 
     a=str1.replace('  ',' ') 
     b=str2.replace('  ',' ') 
     if(len(a)<len(b)): 
         length=len(a) 
     else: 
         length=len(b) 
     count=0 
     for i in range(length): 
         if(a[i]!=b[i]): 
             count=count+1 
     print(length-count) 
 str1=str(input("Enter string 1: ")) 
 str2=str(input("Enter string 2: ")) 
 position(str1, str2)
