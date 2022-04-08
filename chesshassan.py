import time
t1=time.clock()
n=int(input())
X=['A','B','C','D','E','F','G','H']
Y=[1,2,3,4,5,6,7,8]
L=[]
t2=time.clock()
for i in range(n):
    L.append(input())
for i in range(n):
    l=L[i]
    h=l.split()
    xi=l[0]
    yi=int(l[2])
    xf=l[4]
    yf=int(l[6])
    r=X.index(xi)
    s=Y.index(yi)
    f=X.index(xf)
    t=Y.index(yf)
    if (r+s)%2!=(f+t)%2:
        print('Impossible')
    else:
        dxx=r-f
        dyy=s-t
        dx=abs(dxx)
        dy=abs(dyy)
        if dx==0 and dy==0:
            print(0,xi,yi)
        else:
            if dx==dy:
                print(1,xi,yi,xf,yf)
            else:
                li=[]
                lf=[]
                if dyy==0:
                    if dxx>0:
                        while 0<=r<len(X) and s<len(Y) :
                            r=r-1
                            s+=1
                            li.append((r,s))
                        while 0<=f<len(X) and t<len(Y) :
                            f+=1
                            t+=1
                            lf.append((f,t))
                    g= list(set(li) & set(lf))[0][0]
                    v= list(set(li) & set(lf))[0][1]
                    print(2,xi,yi,X[g],Y[v],xf,yf)

print(t2-t1)                   