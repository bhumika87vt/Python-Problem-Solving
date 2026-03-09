#Calculate power using the pow method
n=5
print(pow(n,2))

#Calculate the power without using POW function(using for loop) 
def POW(base,expon):
    res=1
    for i in range(expon):
        res=res*base 
    print(res)
POW(2,6)