n=int(input())
k=0
c=1
while c<n:
    c*=2
    k+=1
if c==n:
    print(n,' ',0)
else:
    if n%2==1:
        print(c,' ',k)
    else:
        s=bin(n)
        j=0
        for i in range(k+2):
            if s[i]=="1":
                j=i-1
        print(c,' ',j)
