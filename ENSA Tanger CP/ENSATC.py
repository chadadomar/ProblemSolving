n=int(input())
l=[]
for i in range(n):
    h=[int(k) for k in input().split()]
    if h[0]==1:
        l.append(h[1])
    elif h[0]==2:
        if len(l)!=0:
            l.pop(-1)
    else:
        if len(l)!=0:
            print(l[-1])