n,m=[int(k) for k in input().split()]
D={}
for i in range(n):
    c,a=[k for k in input().split()]
    a=int(a)
    D[c]=a
for i in range(m):
    k=0
    c=input()
    while(c!='.'):
        L=c.split()
        for c in L:
            if c in D.keys():
                k+=D[c]
        c=input()
    print(k)