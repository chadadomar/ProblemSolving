ch=input()
i=0
j=0
k=0
l=0
for x in ch:
    if x=='_':
        i+=1
    elif ord('A')<=ord(x)<=ord('Z') :
        j+=1
    elif ord('a')<=ord(x)<=ord('z') :
        k+=1
    else:
        l+=1
i=i/len(ch)
j=j/len(ch)
k=k/len(ch)
l=l/len(ch)
print(i)
print(k)
print(j)
print(l)    

a=input()
import math as m
return 4*m.sqrt(a)