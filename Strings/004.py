#To check the palindrome or not
string="abcba"
rev=""
for i in string:
    rev=i+rev
print(rev)
if string==rev:
    print("Palindrome")
else:
    print("not palindrome")