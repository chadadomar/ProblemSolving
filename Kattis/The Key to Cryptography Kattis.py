c=input()
k=input()
l1=len(c)
l2=len(k)
m=''
if l2>=l1:
    for i in range(l1):
        x=(ord(c[i])-ord(k[i]))%26+65
        m+=chr(x)
else:
    for i in range(l2):
        x=(ord(c[i])-ord(k[i]))%26+65
        m+=chr(x)
    for i in range(l2,l1):
        x=(ord(c[i])-ord(m[i-l2]))%26+65
        m+=chr(x)
print(m)