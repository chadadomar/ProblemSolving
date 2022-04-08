n=int(input())
for i in range(n):
    h=int(input())
    s=set()
    k=0
    for i in range(h):
        c=input()
        s.add(c)
    for x in s:
        k+=1
    print(k)