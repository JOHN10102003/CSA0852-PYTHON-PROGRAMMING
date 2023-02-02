def calculate(s: str) -> int: 
     s = s.replace(" ", "") 
     s += '+' 
     st = [] 
     num = 0 
     op = '+' 
     print(s) 
     for i in s: 
         if i.isdigit(): 
             num = (num*10)+int(i) 
         else: 
             num = int(num) 
             if op == '+': 
                 st.append(num) 
             elif op == '-': 
                 st.append(-num) 
             elif op == '*': 
                 st.append(st.pop()*num) 
             elif op == '/': 
                 st.append(int(st.pop()/num)) 
             num = 0 
             op = i 
             print(st) 
     return sum(st) 
 exp=input("Enter the Expression:") 
 print(calculate(exp))
