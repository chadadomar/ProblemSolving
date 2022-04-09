a,b=[int(k) for k in input().split()]
from math import sin,pi
c=a/sin(b*pi/180)
c=int(c)+1
print(c)