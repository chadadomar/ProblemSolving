D={}
n=int(input())
for i in range(n):
    a,b=[k for k in input().split()]
    if 97<=ord(a[0])<=122:
        D[int(b)]=a
    else:
        D[int(a)/2]=b
l=D.keys()
l=sorted(l)
for i in range(n):
    print(D[l[i]])