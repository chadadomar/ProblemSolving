c=input()
e=input()
n=len(c)
m=len(e)
l=max(n,m)
c="0"*(l-n)+c
e="0"*(l-m)+e
flag1=0
flag2=0
C=""
E=""
for i in range(l):
    if int(c[i])<int(e[i]):
        E+=e[i]
    elif int(c[i])>int(e[i]):
        C+=c[i]
    else:
        E+=e[i]
        C+=c[i]
if C=="":
    print("YODA")
else:
    print(int(C))
if E=="":
    print("YODA")
else:
    print(int(E))
        