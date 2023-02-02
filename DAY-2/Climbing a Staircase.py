def fib(n): 
     if(n<0 or n==0): 
         print("Invalid") 
     elif(n==1): 
         return 0 
     elif(n==2): 
         return 1 
     else: 
         return fib(n-1)+fib(n-2) 
 n=int(input("enter a number:")) 
 print("number of ways=",end="") 
 print(fib(n+2))
