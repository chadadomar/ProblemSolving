n=int(input())
s=6*n*n
for i in range(1,n+1):
    if n%i==0:
        m=n//i
        for j in range(1,m+1):
            if m%j==0:
                if 2*(i*j+n//j+n//i) < s :
                    s=2*(i*j+n//j+n//i)
print(s)