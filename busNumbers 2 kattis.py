n=int(input())
l=[int(k) for k in input().split()]
l.sort()
i=0
k=n-1
while i<k:
    h=i
    j=i+1
    while l[j]-l[h]==1:
        j+=1
        h+=1
        print(j)
        print(h)
        print(l[j]-l[h])
        if h==k:
            break
    if j-i>2:
        l[i:j]=[l[i],'-',l[h]]
        k=k-(h-(i+2))
        i+=3
    else:
        i+1
for i in range(k):
    if l[i]=='-' or l[i+1]=='-':
        print(l[i],end='')
    else:
        print (l[i],end=' ')
print(l[-1],end='')
