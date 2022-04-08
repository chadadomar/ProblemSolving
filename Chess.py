import time
t1=time.clock()
n=int(input())
X=['A','B','C','D','E','F','G','H']
Y=[1,2,3,4,5,6,7,8]
L=[]
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
    s=yi-1
    f=X.index(xf)
    t=yf-1
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
                if dxx>=0 and dyy>=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r-1,s-1
                    print(2,xi,yi,X[r],Y[s],xf,yf)
                
                if dxx>=0 and dyy<=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r-1,s+1
                    print(2,xi,yi,X[r],Y[s],xf,yf)
                
                if dxx<0 and dyy>=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r+1,s-1
                    print(2,xi,yi,X[r],Y[s],xf,yf)
                
                if dxx<0 and dyy<=0:
                    while abs(f-r)!=abs(t-s):
                        r,s=r+1,s+1
                    print(2,xi,yi,X[r],Y[s],xf,yf)
t2=time.clock()
print(t2-t1) 