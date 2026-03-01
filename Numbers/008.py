#Factorial of number

#Recursive method
def fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    print(res)
fact(5)