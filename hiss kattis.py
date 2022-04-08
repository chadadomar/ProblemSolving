c=input()
h='no hiss'
for i in range(len(c)-1):
    if c[i]=='s' and c[i+1]=='s':
        h='hiss'
print(h)