d=dict()
c,n=[k for k in input().split()]
n=int(n)
o=input()


#Implement dictionnary of input
l=len(c)
i=0
while i<l :
    if c[i] not in d.keys():
        if i==l-1:
            d[c[i]]=1
            i+=1
        elif 'A'<=c[i+1]:
            d[c[i]]=1
            i+=1
        else:
            j=i+1
            while c[j]<"A" :
                j+=1
                if j==l:
                    break
            d[c[i]]=int(c[i+1:j])
            i=j
    else:
        if i==l-1:
            d[c[i]]+=1
            i+=1
        elif 'A'<=c[i+1]:
            d[c[i]]+=1
            i+=1
        else:
            j=i+1
            while c[j]<"A" :
                j+=1
                if j==l:
                    break
            d[c[i]]+=int(c[i+1:j])
            i=j
#print("d ",d)


for x in d.keys():
    d[x]*=n

#Implement dictionnary of output
s=dict()
l=len(o)
i=0
while i<l :
    if o[i] not in s.keys():
        if i==l-1:
            s[o[i]]=1
            i+=1
        elif 'A'<=o[i+1]<='Z':
            s[o[i]]=1
            i+=1
        else:
            j=i+1
            while o[j]<"A":
                j+=1
                if j==l:
                    break
            s[o[i]]=int(o[i+1:j])
            i=j
    else:
        if i==l-1:
            s[o[i]]+=1
            i+=1
        elif 'A'<=o[i+1]<='Z':
            s[o[i]]+=1
            i+=1
        else:
            j=i+1
            while o[j]<"A":
                j+=1
                if j==l:
                    break
            s[o[i]]+=int(o[i+1:j])
            i=j
#print("s ",s)
l=[]
flag=True
for x in s.keys():
    if x  in d.keys():
        l.append(d[x]//s[x])
    else:
        print(0)
        flag=False
        break
if flag:
    print(min(l))