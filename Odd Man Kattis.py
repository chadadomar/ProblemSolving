n=int(input())
k=0
for i in range(n):
    k=int(k)
    k+=1
    G=int(input())
    l=[int(k) for k in input().split()]
    while len(l)>=3:
        h=len(l)
        for j in range(1,h):
            if l[0]==l[j]:
                del(l[j])
                del(l[0])
                break
        if h==len(l):
            x=l[0]
            break
    x=l[0]
    k=str(k)
    x=str(x)
    print("Case #"+k+": "+x)
