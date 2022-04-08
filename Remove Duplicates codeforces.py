n=int(input())
h=[int(k) for k in input().split()]
e=[]
for i in range(n):
    if h[i] in e:
        e.remove(h[i])
        e.append(h[i])
    else:
        e.append(h[i])
print(len(e))
for x in e:
    print(x,end=' ')
