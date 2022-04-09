K=[k for k in input().split()]
l=['a','e','i','o','u']
for c in K:
    k=len(c)
    d=""
    i=0
    while i<k:
        if c[i] in l:
            d+=c[i]
            i+=3
        else:
            d+=c[i]
            i+=1
    print(d,end=' ')