n,m=[int(k) for k in input().split()]
a=[0]+[int(k) for k in input().split()]
b=[int(k) for k in input().split()]
for i in range(m):
    c=0
    j=0
    while b[i]>c and j<n:
        j+=1
        c+=a[j]
    print(j,' ',b[i]+a[j]-c)

        