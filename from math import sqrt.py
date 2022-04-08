from math import sqrt
n=int(input())
l=[]
for i in range(n):
    l.append([int(k) for k in input().split()])
q=int(input())
for i in range(q):
    x1,y1,x2,y2,z=[int(k) for k in input().split()]
    a=(y1-y2)/(x1-x2)
    b=y1-a*x1
    flag=True
    for j in range(n):
    	if z>l[j][-1]:
    		continue
    	elif z==l[j][-1]:
    		if l[j][1]==a*l[j][0]+b:
    			print("NO")
    			flag=False
    			break
    	else:
    		r=l[j][2]*z/l[j][-1]
    		d=abs(-a*l[j][0]+l[j][1]-b)/(sqrt(a*a+b*b))
    		if d<=r:
    			print("NO")
    			flag=False
    			break
    if flag==True :
    	print("YES")
    	
    
