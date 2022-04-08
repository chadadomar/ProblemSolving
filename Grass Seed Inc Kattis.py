c=float(input())
l=int(input())
k=0
for i in range(l):
    a,b=[float(k) for k in input().split()]
    k+=a*b
t=k*c
t=round(t,7)
print(t)
