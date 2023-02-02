def happy(n): 
    t=n 
    sum=0 
    while(t>0): 
       d=t%10 
       sum+=d**2 
       t//=10 
    return sum 
 n=int(input("enter the number:")) 
 r=n 
 while r!=1 and r!=4: 
     r=(happy(r)) 
 if r==1: 
     print("True") 
 elif r==4: 
     print("False")
