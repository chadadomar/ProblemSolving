n=int(input())
if n==2:
    print(1)
    print(1," ",1)
elif n%2==0:
    k=n/2
    if k%2==0:
        print(0)
        print(int(k),end=' ')
        l=[(2*i+1) for i in range(int(k/2))]
        l+=[(2*i) for i in range(1+int(k/2),int(k)+1)]
        for x in l:
             print(x,end=' ')
    else:
        print(1)
        print(int(k+1), end=' ')
        l=[(2*i+1) for i in range(int(k/2)+1)]
        l+=[(2*i) for i in range(2+int(k/2),int(k)+1)]
        for x in l:
             print(x,end=' ')
else:
    k=(n-1)/2
    if n==3:
        print(0)
        print(2,1,2)
    else:
        if k%2==1:
            print(0)
            print(int(k)+1,1,end=' ')
            l=[(2*i) for i in range(1,int(k/2)+2)]
            l+=[(2*i+1) for i in range(2+int(k/2),int(k)+1)]
            for x in l:
                print(x,end=' ')
        else:
            print(1)
            print(int(k+1),1,end=' ')
            l=[(2*i) for i in range(1,int(k/2)+1)]
            l+=[(2*i+1) for i in range(1+int(k/2),int(k)+1)]
            for x in l:
                print(x,end=' ')