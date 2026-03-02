#prime number or not
n=37
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
    else:
        print("Prime")
else:
    print("Not Prime")