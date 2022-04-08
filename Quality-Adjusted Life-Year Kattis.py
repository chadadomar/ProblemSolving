n=int(input())
s=0
for i in range(n):
    a,b=[float(k) for k in input().split()]
    s+=a*b
s=round(s,3)
print(s)
    