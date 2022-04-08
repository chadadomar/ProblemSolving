t=int(input())
for i in range(t):
    n,k=[int(s) for s in input().split()]
    l=[int(s) for s in input().split()]
    d=[]
    w=[]
    j=0
    while(j<n):
        if l[j]==1:
            if d!=[]:
                w.append(d)
            d=[]
            j+=1
        else:
            d.append(l[j])
            j+=1
    w.append(d)
    #print(w)
    sum=0
    for e in w:
        if e!=[]:
            #print(max(e))
            sum+=max(e)-1
    print(sum)
    