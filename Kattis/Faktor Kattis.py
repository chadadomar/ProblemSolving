c=input()
T,C,G,k=0,0,0,1
for i in range(len(c)):
    if c[i]=='T':
        T+=1
        k*=2
    elif c[i]=='C':
        C+=1
        k*=3
    else:
        G+=1
        k*=5
i=1
while k%(30**i)==0:
    i+=1
print(T*T+C*C+G*G+7*(i-1))