n=int(input())
d=dict()
s=dict()
for i in range(n):
    c1=input()
    c2=input()
    d[c1]=c2
    s[c1]=0
m=int(input())

for i in range(m):
    c=input()
    if c in d.keys():
        s[c]+=1
l=[]
for x in s.keys():
    l.append([s[x],x])
l.sort()
if l[-1][0]==l[-2][0]:
    print("tie")
else:
    d[l[-1][1]]
    
    