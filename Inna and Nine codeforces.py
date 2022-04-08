c=input()
k=len(c)
if k==1:
    print(1)
else:
    l=[]
    n=1
    flag=0
    for i in range(k-1):
        if int(c[i])+int(c[i+1])==9:
            if i not in l:
                l.append(i)
            l.append(i+1)
    for x in l:
        print(x,end=' ')
    t=len(l)
    for i in range(t-1):
        if l[i+1]-l[i]==1:
            flag+=1
        else:
            if (flag+1)%2==1:
                n*=(flag+2)/2
    print(n)
                       