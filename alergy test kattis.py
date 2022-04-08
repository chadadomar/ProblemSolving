k=int(input())
d=[]
for i in range(k):
    d.append(int(input()))
d.sort()
add=0
index=0
for i in range(k):
    if d[i]>1:
        index=i
        break
    else:
        add+=1
l=d[index:]
