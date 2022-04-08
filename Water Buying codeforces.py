q=int(input())
for i in range(q):
    n,a,b=[int(k) for k in input().split()]
    if b>=2*a:
        print(a*n)
    else:
        y=n//2
        x=n-2*y
        print(a*x+b*y)
