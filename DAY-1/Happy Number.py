def sumsquare(n):
    sq=0
    while(n!=0):
        digit = n%10
        sq+=digit*digit
        n//=10
    return sq

def happy(n):
    s=set()
    s.add(n)
    while(True):
        if(n==1):
            return True
        n=sumsquare(n)
        if n in s:
            return False
        s.add(n)
    return False

n=int(input("Enter a number: "))
if(happy(n)):
    print("YES, n is happy :)")
else:
    print("NO, n is sad :(")
