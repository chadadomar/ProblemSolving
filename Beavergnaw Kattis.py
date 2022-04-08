def dico(f,a,b,e):
    while abs(a-b) > e:
        x=(a+b)/2
        if f(a)*f(x) < 0 :
            b=x
        else:
            a=x
    return x

from math import pi
D,V=[int(k) for k in input().split()]
while D!=0 and V!=0 :
    def f(x):
        return D*D*D*pi/4-x*x*x*pi/4-(D-x)*pi*(D*D+x*x+D*x)/3-V
    c=dico(f,0,D,0.00000001)
    print(c)
    D,V=[int(k) for k in input().split()]
    