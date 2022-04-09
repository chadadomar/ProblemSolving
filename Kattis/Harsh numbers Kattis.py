def isHarsh(n):
    s=sum([int(k) for k in str(n)])
    r=n%s
    return r
n=int(input())
i=n
while(isHarsh(i)!=0):
    i+=1
print(i)