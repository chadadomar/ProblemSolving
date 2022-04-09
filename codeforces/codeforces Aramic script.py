n=int(input())
h=input().split()
l=[]
for i in range(n):
    s=set()
    k=len(h[i])
    for j in range(k):
        s.add(h[i][j])
    if s not in l:
        l.append(s)
print(len(l))