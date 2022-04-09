D={'A':11,'K':4,'Q':3,'T':10,'8':0,'7':0}
n,b=[k for k in input().split()]
n=int(n)
k=0
for i in range(4*n):
    c=input()
    if c[0]=='9':
        if c[1]==b:
            k+=14
    elif c[0]=='J':
        if c[1]==b:
            k+=20
        else:
            k+=2
    else:
        k+=D[c[0]]
print(k)
            
    