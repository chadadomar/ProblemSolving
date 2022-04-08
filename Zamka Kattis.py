l=int(input())
d=int(input())
x=int(input())
L=[]
for i in range(l,d+1):
    k=0
    c=str(i)
    for t in c:
        k+=int(t)
    if k==x:
        L.append(i)
print(L[0])
print(L[-1])

    