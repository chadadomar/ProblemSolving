l=input().split()
h=int(l[0])
t=len(l)
if t==1 :
    print(pow(2,h+1)-1)
else:
    s=l[1]
    k=len(s)
    if s[0]=='L':
        position=0
    else:
        position=1
    if k>1 :
        for i in range(1,k):
            if s[i]=='L':
                position=2*position
            else:
                position=2*position+1
    print(pow(2,h+1)-pow(2,k)-position)
    