c=[int(k) for k in input().split()]
c.sort()
if c[1]-c[0]==c[2]-c[1]:
    print(c[2]+c[1]-c[0])
elif c[1]-c[0]<c[2]-c[1]:
    print(c[1]+c[1]-c[0])
else:
     print(c[0]+c[2]-c[1])
