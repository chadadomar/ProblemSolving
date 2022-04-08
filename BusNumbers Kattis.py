import time
t1=time.clock()
n=int(input())
l=[ int(k) for k in input().split()]
l.sort()
h=[]
i=0
while i<n-2:
    if l[i+2]-l[i]==2:
        h.append(l[i])
        h.append(-)
        j=i+2
        while l[j+1]-l[j]==1 and j<n-1:
            j+=1
        h.append(l[j])
        h.append(' ')
        i=j+1
    else:
        h.append(l[i])
        h.append(' ')
        h.append(l[i+1])
        h.append(' ')
        h.append(l[i+2])
        h.append(' ')
        i+=2
for c in h:
    print(c,end='')
        
                
        
    

t2=time.clock()    
print(t2-t1)

        
        
    
        
