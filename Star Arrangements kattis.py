n=int(input())
print(str(n)+":")
from math import sqrt
l=[]
for a in range(1,1+(n-2)//3):
    if (n-a-1)%(2*a+1)==0:
        l.append([a+1,a])
for a in range(1,int(sqrt(n))+1):
    if n%a==0:
        b=n//a
        if a%2==1:
            if a!=1:
                l.append([(a+1)//2,(a-1)//2])
        if b%2==1:
            l.append([(b+1)//2,(b-1)//2])
        if a!=1:
            l.append([a,a])
            if b!=a:
                l.append([b,b])
l.sort()
for x in l:
    print(str(x[0])+","+str(x[1]))