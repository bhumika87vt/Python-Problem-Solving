#Amstrong Number
n=153
count=len(str(n))
sum=0
for i in str(n):
    sum=sum+int(i)**count
if sum==n:
    print("Amstrong number")
else:
    print("Not Amstrong number")