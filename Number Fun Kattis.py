n=int(input())
for i in range(n):
    l=[int(k) for k in input().split()]
    a=l[0]+l[1]
    b=l[0]*l[1]
    c=l[0]/l[1]
    d=l[1]/l[0]
    e=l[0]-l[1]
    f=l[1]-l[0]
    if l[2] in [a,b,c,d,e,f]:
        print('Possible')
    else:
        print('Impossible')
        