t=int(input())
from math import sqrt
for i in range(t):
    n,e=[int(k) for k in input().split()]
    p=1
    if n%2==0:
        p=2
    else:
        for j in range(2,int(sqrt(n)+1)):
            if n%j==0:
                p=j
                break
    q=n//p
    phi=(p-1)*(q-1)
    for d in range(2,phi):
        if (d*e-1)/phi==int((d*e-1)/phi):
            print(d)
            break
        