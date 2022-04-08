a,b=[k for k in  input().split()]
n=int(a)
t=float(b)
while n+t!=0:
    f=2**n
    for i in range(1,n+1):
        f=max(2**(n-i),(1+t)*f/2)
    print(f)
    a,b=[k for k in  input().split()]
    n=int(a)
    t=float(b)