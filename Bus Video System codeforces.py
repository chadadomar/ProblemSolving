n,w=[int(k) for k in input().split()]
a=[int(k) for k in input().split()]
mx,mn,sum=0,0,0
for i in range(n):
    sum+=a[i]
    mx=max(mx,sum)
    mn=min(mn,sum)
print(max(0,w-mx+mn+1))
