t=int(input())
for i in range(t):
    n=int(input())
    l=[int(k) for k in input().split()]
    if n==1:
        print(0)
    else:
        i=0
        u=1
        while i <len(l)-1:
            if i<0:
                i=0
            if l[i]>l[i+1]:
                a=l[i+1]+1
                t=l[i]
                for j in range(u,l[i+1]+1):
                    l.remove(j)
                i=l.index(t)
                u=a
            else:
                i+=1
        print(n-len(l))
