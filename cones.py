
import math
def calculerDelta(a,b,c):
   return b*b-4*a*c

def resoudreEquationSecondDegre(a,b,c):
   delta = calculerDelta(a,b,c)
   if delta > 0:
      racineDeDelta=math.sqrt(delta)
      retour = [(-b-racineDeDelta)/(2*a),(-b+racineDeDelta)/(2*a)]
   elif delta < 0:
      retour = []  #liste vide
   else:
      retour = [-b/(2*a)] #liste d'un seul élément
   return retour


n=int(input())
l=[]
for i in range(n):
    l.append([int(k) for k in input().split()])
q=int(input())
for i in range(q):
    x1,y1,x2,y2,z=[float(k) for k in input().split()]
    a=(y1-y2)/(x1-x2)
    b=y1-a*x1
    flag=True
    for j in range(n):
    	if z>l[j][-1]:
    		continue
    	elif z==l[j][-1]:
    		if l[j][1]==a*l[j][0]+b:
    			if (min(x1,x2)<=l[j][0] and max(x1,x2)>=l[j][0]) or (min(y1,y2)<=l[j][1] and max(y1,y2)>=l[j][1]):
    				print("NO")
    				flag=False
    				break
    	else:
    		r=l[j][2]*(l[j][-1]-z)/l[j][-1]
    		'''#print(r)
    		d=abs(-a*l[j][0]+l[j][1]-b)/(sqrt(a*a+1))

    		#print(d)
    		if d<=r:
    			print("NO")
    			flag=False
    			break'''
    		t=1+a*a
    		y=2*(a*(b-l[j][1])-l[j][0])
    		u=l[j][0]*l[j][0]+(b-l[j][1])*(b-l[j][1])-r*r
    		i=resoudreEquationSecondDegre(t,y,u)
    		if len(i)>=1:
    			xint=i[0]
    			yint=a*xint+b
    			if (min(x1,x2)<=xint and max(x1,x2)>=xint) or (min(y1,y2)<=yint and max(y1,y2)>=yint):
    				print("NO")
    				flag=False
    				break
    if flag==True :
    	print("YES")