N=int(input())
p='ABC'
q='BABC'
r='CCAABB'
if N/6 is int:
    R=N/6
else:
    R=N//6 +1
if N/4 is int:
    Q=N/4
else:
    Q=N//4 +1
if N/3 is int:
    P=N/3
else:
    P=N//3 +1
p*=P
q*=Q
r*=R
a,b,c=0,0,0
C=input()
for i in range(N):
    if C[i]==p[i]:
        a+=1
    if C[i]==q[i]:
        b+=1
    if C[i]==r[i]:
        c+=1
d=max(a,max(b,c))
print(d)
if a==d:
    print('Adrian')
if d==b:
    print('Bruno')
if d==c:
    print('Goran')

    
