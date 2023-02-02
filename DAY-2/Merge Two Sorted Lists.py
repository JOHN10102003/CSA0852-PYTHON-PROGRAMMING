l1 = [] 
 l2=[] 
 n=int(input("Enter number of elements : ")) 
 for i in range(0, n): 
     a=int(input()) 
     l1.append(a) 
 print(l1) 
 n2=int(input("Enter number of elements : ")) 
 for i in range(0, n2): 
     b=int(input()) 
     l2.append(b) 
 print(l2) 
 s=l1+l2 
 print(sorted(s))
