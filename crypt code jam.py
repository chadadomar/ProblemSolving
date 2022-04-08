def gcd(x1,x2):
    if x2==0:
        return x1
    else:
        return gcd(x2,x1%x2)

t=int(input())
for i in range(t):
    n,l=[int(k) for k in input().split()]
    c=[int(k) for k in input().split()]
    u=gcd(c[0],c[1])
    P=[]
    P.append(c[0]//u)
    P.append(u)
    temp=u
    for j in range(1,l):
        P.append(c[j]//temp)
        temp=c[j]//temp
    #print("P", P)
    W=[]
    for e in P:
        if e not in W:
            W.append(e)
    W.sort()
    #print("W",W)
    #print("S",S)
    count=65
    for e in W:
        D[e]=chr(count)
        count+=1
    #print("count",count-65)
    #print("Dict",D)
    ch=""
    #print("P[0]",P[0])
    #print("D[P[0]]",D[P[0]])
    for j in range(l+1):
        ch+=D[P[j]]
    print("Case #"+str(i+1)+": "+ch)
        