n=int(input())
c=input()
e=set()
for i in range(n-1):
    e.add(c[i]+c[i+1])
a={}
for x in e:
    k=0
    for i in range(n-1):
        if x==(c[i]+c[i+1]):
            k+=1
    a[str(k)]=x
z=max([int(s) for s in a.keys()])
print(a[str(z)])
