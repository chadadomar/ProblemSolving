l="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
h=input().split()
a=int(h[0])
while a!=0:
    c=h[1]
    d=len(c)
    e=""
    for i in range(1,d+1):
        if c[d-i]==".":
            e+=l[a-1]
        elif c[d-i]=="_":
            e+=l[(a+26)%28]
        else:
            e+=l[(a+ord(c[d-i])-65)%28]
    print(e)
    h=input().split()
    a=int(h[0])        