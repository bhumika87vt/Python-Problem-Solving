#To count occurrence of a given string
s='abcba'
ch='a'
count=0
for i in s:
    if i==ch:
        count+=1

print(count)