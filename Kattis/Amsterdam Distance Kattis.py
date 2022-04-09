from math import pi
b=[k for k in input().split()]
m=int(b[0])
n=int(b[1])
r=float(b[2])
x,y,z,t=[int(k) for k in input().split()]
s=abs(y-t)*r/n+abs(x-z)*pi*min(y,t)*r/(m*n)
v=(y+t)*r/n
print(min(s,v))