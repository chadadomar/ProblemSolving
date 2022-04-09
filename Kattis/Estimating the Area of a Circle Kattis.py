from math import pi
for i in range(1000):
    r,m,c=[float(k) for k in input().split()]
    m=int(m)
    c=int(c)
    if r==0 and c==0 and m==0:
        break
    else:
        s=pi*r*r
        s=round(s,9)
        a=4*r*r*c/m
        a=round(a,9)
    print(s,' ',a)
