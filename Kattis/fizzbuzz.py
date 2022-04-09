n=int(input())
X=['A','B','C','D','E','F','G','H']
Y=[1,2,3,4,5,6,7,8]
L=[0]*n
for i in range(n):
    L[i]=input()
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
        print('impossible')
    else:
        dxx=r-f
        dyy=s-t
        dx=abs(dxx)
        dy=abs(dyy)
        if dx==0 and dy==0:
            print(0,x,y)
        else:
            if dx==dy:
                print(1,x,y,a,b)
            else:
                if dxx>=0 and dyy>=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r-1,s-1
                    print(2,x,y,X[r],Y[s],a,b)
                
                if dxx>=0 and dyy<=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r-1,s+1
                    print(2,x,y,X[r],Y[s],a,b)
                
                if dxx<=0 and dyy>=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r+1,s-1
                    print(2,x,y,X[r],Y[s],a,b)
                
                if dxx<=0 and dyy<=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r+1,s+1
                    print(2,x,y,X[r],Y[s],a,b)