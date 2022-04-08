l=[]
e=set()
n=int(input())
for i in range(n):
    d,t=[int(k) for k in input().split()]
    e.add(t)
    e.add(t-d)
    e.add(t-2*d)
    l.append(t)
    l.append(t-d)
    l.append(t-2*d)
d=dict()
for x in e:
    d[x]=l.count(x)
m=max(d.values())
if m%2==0:
    print(m//2)
else:
    print(m//2+1)