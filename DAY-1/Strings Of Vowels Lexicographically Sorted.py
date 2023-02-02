def solve(n):
   if n==1:
      return 5
   count = [1 for i in range(6)]
   for i in range(3,n+1):
      count[1] = count[1]+count[2]+count[3]+count[4]+count[5]
      count[2] = count[2]+count[3]+count[4]+count[5]
      count[3] = count[3]+count[4]+count[5]
      count[4] = count[4]+count[5]
   total = 0
   for i in range(1,6):
      total += i*count[i]
   return total
n = int(input("Enter the value of n:"))
print(solve(n))
