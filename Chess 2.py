def check(a,b):
	if 1<=a<=8 and 1<=b<=8:
		return True
	else:
		return False


n=int(input())
for h in range(n):
    l=[k for k in input().split()]
    c1=l[0]
    p1=ord(c1)-64
    r1=int(l[1])
    c2=l[2]
    p2=ord(c2)-64
    r2=int(l[3])
    if ((p1+r1)%2)!=((p2+r2)%2):
    	print('Impossible')
    elif r1==r2 and c2==c1 :
    	print("0 "+c1+" "+str(r1))
    else:
    	#possible moves for first chessman
    	M1=[]
    	for i in range(1,8):
    		a=p1+i
    		b=r1+i
    		if check(a,b):
    			M1.append([a,b])

    		a=p1+i
    		b=r1-i
    		if check(a,b):
    			M1.append([a,b])

    		a=p1-i
    		b=r1+i
    		if check(a,b):
    			M1.append([a,b])

    		a=p1-i
    		b=r1-i
    		if check(a,b):
    			M1.append([a,b])
    	#si second position in M1
    	if [p2,r2] in M1:
    		print("1 "+c1+" "+str(r1)+" "+c2+" "+str(r2))
    	else:
    		#possible moves for first chessman
	    	M2=[]
	    	for i in range(1,8):
	    		a=p2+i
	    		b=r2+i
	    		if check(a,b):
	    			M2.append([a,b])

	    		a=p2+i
	    		b=r2-i
	    		if check(a,b):
	    			M2.append([a,b])

	    		a=p2-i
	    		b=r2+i
	    		if check(a,b):
	    			M2.append([a,b])

	    		a=p2-i
	    		b=r2-i
	    		if check(a,b):
	    			M2.append([a,b])
	    	for i in range(len(M2)):
	    		if M2[i] in M1:
	    			p3=M2[i][0]
	    			c3=chr(p3+64)
	    			r3=M2[i][1]
	    			print("2 "+c1+" "+str(r1)+" "+c3+" "+str(r3)+" "+c2+" "+str(r2))
	    			break


