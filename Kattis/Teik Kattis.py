c=input()
l=[1,0,0]
j=len(c)
for i in range(j):
    if c[i]=='A':
        l[0],l[1]=l[1],l[0]
    if c[i]=='B':
        l[1],l[2]=l[2],l[1]
    if c[i]=='C':
        l[2],l[0]=l[0],l[2]
y=l.index(1)+1
print(y)