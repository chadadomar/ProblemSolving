n=int(input())
for i in range(n):
    s=0
    l=[int(k) for k in input().split()]
    N=l[0]
    for i in range(1,N+1):
        s+=l[i]
    s=float(s/N)
    k=0
    for i in range(1,N+1):
        if l[i]>s:
            k+=1
    r=100*float(k/N)
    c="%.3f"%r
    c=str(c)
    print(c+"%")