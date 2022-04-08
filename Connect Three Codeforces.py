xa,ya=[int(k) for k in input().split()]
xb,yb=[int(k) for k in input().split()]
xc,yc=[int(k) for k in input().split()]
D={}
D[xa]=ya
D[xb]=yb
D[xc]=yc
X=[xa,xb,xc]
Y=[ya,yb,yc]
X.sort()
Y.sort()
ans=X[2]-X[0]+Y[2]-Y[0]+1
print(ans)
for i in range(Y[0],Y[2]+1):
    print(X[1],i)
for i in range(X[0],X[1]):
    print(i,D[X[0]])
for i in range(X[1]+1,X[2]+1):
    print(i,D[X[2]])
