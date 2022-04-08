n=int(input())
l=[int(k) fot k in input().split()]
print(l[0])
i=0
j=0
while i<N-1:
    j=i+1
    while j<N:
    if l[j]<=l[i]:
        j+=1
    else:
        print(l[j])
        i=j
