def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n - 1);
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
n = int(input("Enter the number: "))
print("Factorial of",n,"is",fact(n))
print("\n")
print("And the factors of",n,"are: ")
factors(n)
