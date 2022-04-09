r,c=[int(k) for k in input().split()]
c=[]
for i in range(r):
    c.append(input())
i,j,k=0,0,0
while(c[i][j]!='T'):
    if c[i][j]=='N':
        i-=1
        k+=1
    elif c[i][j]=='S':
        i+=1
        k+=1
    elif c[i][j]=='W':
        j-=1
        k+=1
    else:
        j+=1
        k+=1
print(k)
