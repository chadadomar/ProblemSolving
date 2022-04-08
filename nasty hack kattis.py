l=[int(k) for k in input().split()]
h=[1,1,2,2,2,8]
for i in range(5):
    print(h[i]-l[i],end=' ')
print(h[-1]-l[-1],end=' ')