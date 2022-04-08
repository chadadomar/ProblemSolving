t=int(input())
for w in range(t):
    n=int(input())
    s=6*n
    D={"harira":n, "baghrira":n, "rghifa":n, "dates":n, "egg" :n, "atay":n}
    for i in range(n):
    	l=[k for k in input().split()]
    	t=int(l[0])
    	s-=t
    	for j in range(t):
    		c=l[j+1]
    		D[c]-=1
    print(s)
    print(D["harira"],"harira")
    print(D["baghrira"],"baghrira")
    print(D["rghifa"],"rghifa")
    print(D["dates"],"dates")
    print(D["egg"],"egg")
    print(D["atay"],"atay")