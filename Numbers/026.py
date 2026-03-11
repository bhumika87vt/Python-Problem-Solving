#GCD of two numbers using recursion
def GCD(a,b):
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i 
    print(gcd)
GCD(12,18)