n=int(input("Enter the row limit: "))
for i in range(1,n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
    for j in range(i,0,-1):
        print(' ', i, sep='', end='')
        i-=1
    print()
