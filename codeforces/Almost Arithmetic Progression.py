n=int(input())
b=[int(k) for k in input().split()]
b.sort()
if int((b[-1]-b[0])/(n-1))==(b[-1]-b[0])/(n-1):
    k=(b[-1]-b[0])/(n-1)
else:
    k=int((b[-1]-b[0])/(n-1))+1
#print("k ",k)
import sys
m=0
if n==1 or n==2:
    print('0')
else:
    for i in range(n-1):
        if b[i+1]-b[i]<k-2 or b[i+1]-b[i]>k+2:
            print("-1")
            sys.exit(0)
        else:
            if b[i+1]-b[i]!=k:
                m+=1
    print(m)