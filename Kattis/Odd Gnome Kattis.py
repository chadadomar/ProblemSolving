n=int(input())
for i in range(n):
    l=[int(k) for k in input().split()]
    s=len(l)
    for j in range(1,s-1):
        if l[j+1]-l[j]!=1:
            print(j+1)
            break