n=int(input())
L=[]
H=[]
j=0
for i in range(n):
    if j==12:
        break
    else:
        a,b=[k for k in input().split()]
        if a  not in L:
            L.append(a)
            H.append(b)
            j+=1
for i in range(12):
    print(L[i],' ',H[i])