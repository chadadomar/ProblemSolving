t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    l.append([1,2,3,4,5,6,7,8,9,10])
    for h in range(n-1):
        l.append([0]*10)
    for j in range(1,n):
        if j%2==0:
            l[j][0]=l[j-1][0]
            for k in range(1,10):
                l[j][k]=l[j-1][k]+l[j][k-1]
        if j%2==1:
            l[j][-1]=l[j-1][-1]
            for k in range(8,-1,-1):
                l[j][k]=l[j][k+1]+l[j-1][k]
    print(l)
    if n%2==0:
        print(l[-1][1])
    else:
        print(l[-1][-2])