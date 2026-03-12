#To remove a given character from a string
s='abcde'
res=''
for i in s:
    if i!='e':
        res=res+i #or res.replace('e','')
print(res)