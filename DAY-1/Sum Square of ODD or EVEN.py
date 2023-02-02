def sumsquare(l): 
     odd=[] 
     even=[] 
     l2=[] 
     for i in range(len(l)): 
         if l[i]%2==0: 
             even.append(l[i]) 
         else: 
             odd.append(l[i]) 
     print(odd) 
     print(even) 
     odds=sum([x**2 for x in odd]) 
     l2.append(odds) 
     evens=sum([y**2 for y in even]) 
     l2.append(evens) 
     return l2 
  
 n=int(input("enter the number :")) 
 l=[] 
 while True: 
     num=int(input("enter the element:")) 
     l.append(num) 
     if len(l)==n: 
         break 
 print(l) 
 print(sumsquare(l))
