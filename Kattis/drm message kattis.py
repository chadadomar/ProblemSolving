c=input()
k=len(c)
l1=[]
l2=[]
for i in range(k//2):
    l1.append(c[i])
for i in range(k//2,k):
    l2.append(c[i])
s=0
for i in range(k//2):
    s+=ord(l1[i])-65
for i in range(k//2):
    l1[i]=chr( ( ord(l1[i])-65 +s)%26 + 65)
m=0
for i in range(k//2):
    m+=ord(l2[i])-65
for i in range(k//2):
    l2[i]=chr( ( ord(l2[i])-65 +m)%26 + 65)
for i in range(k//2):
    l1[i]=chr( ( ord(l1[i])%26+ord(l2[i])%26)%26 + 65)
for i in range(k//2):
    print(l1[i],end='')


