def count(s,c):
    c=0
    for i in s:
        if i==c:
            c+=1
    return c

s=input()
n=len(s)
c1=2*count(s,'D')
c2=2*count(s,'U')
c3=0
for i in range(n-1):
    if s[i]!=s[i+1]:
        c3+=1
print(c1)
print(c2)
print(c3)