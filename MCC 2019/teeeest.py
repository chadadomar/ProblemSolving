t=int(input())
for e in range(t):
    n,k=[int(k) for k in input().split()]
    l=[]
    H=[]
    for i in range(n):
        a,b=[int(k) for k in input().split()]
        l.append([a,b])
        H.append(a)
    w=[]
    for i in range(n-k):
        m=min(H[i:i+k])
        M=max(H[i:i+k])
        tst=0
        for j in range(i,i+k):
            tst+=abs(l[j][0]-m)*l[j][1]
        rslt=tst
        for s in range(m+1,M+1):
            tst=0
            for j in range(i,i+k):
                tst+=abs(l[j][0]-s)*l[j][1]
            if tst<rslt:
                rslt=tst
        w.append(rslt)
    print(min(w))