n=int(input("Enter the row limit: ")) 
 for i in range(1,n+1): 
     for j in range(0, n-i+1): 
         print(' ', end='') 
     c=1 
     for j in range(1,i+1): 
         print(' ', c, sep='', end='') 
         c=c*(i-j)//j 
     print()
