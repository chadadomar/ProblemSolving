a,b=[k for k in input().split()]
L=[c for c in a]
H=[c for c in b]
c1=''
c2=''
for i in range(2,-1,-1):
    c1+=L[i]
    c2+=H[i]
a=int(c1)
b=int(c2)
print(max(a,b))
