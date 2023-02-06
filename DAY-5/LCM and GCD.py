def gcd(a,b):
    while(b):
        a,b=(b, a%b)
    return a

def lcm(a,b):
    lcm=(a*b)//gcd(a,b)
    return lcm

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print("LCM = ",lcm(a,b))
print("GCD = ",gcd(a,b))
