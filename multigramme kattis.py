def gcd(x1,x2):
    if x2==0:
        return x1
    else:
        return gcd(x2,x1%x2)

ch=input()
N=""
l=len(ch)
for i in range(l):
    if ch[i] not in N:
        N+=ch[i]
q=len(N)
t=[0]*q
for i in range(q):
    for j in range(l):
        if ch[j]==N[i]:
            t[i]+=1
g=t[0]
for i in range(q):
    g=gcd(t[i],g)
if g==1:
    print("-1")
else:
    #print("g is: ",g)
    for tst in range(g,1,-1):
        if l%tst==0:
            o=int(l/tst)
            b=ch[:o]
            #print("b is: ",b)
            ens=set(k for k in b)
            for i in range(1,tst):
                z=ch[i*o:(i+1)*o]
                #print("z is: ",z)
                flag=1
                ens2=set(k for k in z)
                if ens2!=ens:
                    flag=0
                    break
            #print("flag=",flag)
            if flag==1:
                print(b)
                break