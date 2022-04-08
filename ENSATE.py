a=list(input())
b=list(input())
n=len(a)
c=set()
e=set()
for i in range(n):
    c.add(a[i])
    e.add(b[i])
if c==e:
    flag=True
    for i in c:
        if a.count(i)!=b.count(i):
            flag=False
            break
    if flag==True:
        print("YES")
    else:
        print("NO")
else:
    print("NO")