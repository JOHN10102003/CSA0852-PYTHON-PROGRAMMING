M = int(input("Enter the starting number-M: "))
N = int(input("Enter the ending number-N: "))
K = int(input("Enter the numbers to be skipped in range-K: "))
for i in range(M, N+1, K+1):
    print(i)
