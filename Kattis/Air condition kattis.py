n=int(input())
l=[]
h=[int(k) for k in input().split()]
l.append(h)
for i in range(n-1):
    flag=True
    h=[int(k) for k in input().split()]
    #print(h)
    for i in range(len(l)):
        a=max(l[i][0],h[0])
        b=min(l[i][1],h[1])
        #print(x)
        if a<=b:
            l[i]=[a,b]
            flag=False
            continue
    if flag==True:
        l.append(h)
#print("l ",l)
print(len(l))