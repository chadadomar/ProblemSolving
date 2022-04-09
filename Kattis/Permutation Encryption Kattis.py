L=[int(k) for k in input().split()]
n=L[0]
while(n!=0):
    c=input()
    k=len(c)
    r=k%n
    if r!=0:
        c+=' '*(n-r)
        k=k+n-r
    new=''
    q=k//n
    #print(q)
    for i in range(q):
        for j in range(n):
            p=L[j+1]
            #print(p)
            #print(p)
            #print(c[q*i+p-1])
            #print(n*i+p-1)
            new+=c[n*i+p-1]
    print("'"+new+"'")
    L=[int(k) for k in input().split()]
    n=L[0]
    if(n==0):
        quit
    