b,k=[int(k) for k in input().split()]
a=[int(k) for k in input().split()]
if b%2==0:
    if a[-1]%2==0:
        print("even")
    else:
        print("odd")
else:
    c=sum(a)
    if c%2==0:
        print("even")
    else:
        print("odd")