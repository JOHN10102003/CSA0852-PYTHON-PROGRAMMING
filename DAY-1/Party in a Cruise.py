tot=int(input("enter the value of t:")) 
 e=[7,0,8,4,2] 
 l=[1,2,3,1,2] 
 x=[0,0,0,0,0] 
 for i in range(0,tot): 
     x[i]=x[i-1]+e[i]-l[i] 
     print(x[i]) 
 print("max guest=",max(x))
