def f(n,m):
    print((n+m)//2)
    c=input()
    if c=="lower":
        f(n,(n+m)//2)
    elif c=="higher":
        if (n+m)//2==m-1:
            print(m)
        else:
            f((n+m)//2,m)
f(0,1000)
    