import random

def trans(a,b,c,d):
    return d+10*c+100*b+1000*a

l=[0,1,2,3,4,5,6,7,8,9]
a1=random.choice(l)
l.remove(a1)
b1=random.choice(l)
l.remove(b1)
c1=random.choice(l)
l.remove(c1)
d1=random.choice(l)
l.remove(d1)

print(trans(a1,b1,c1,d1))
x=int(input("chban lik "))
a2=int(str(x)[0])
b2=int(str(x)[1])
c2=int(str(x)[2])
d2=int(str(x)[3])

if a2==0:
	a1=random.choice(l)
	l.remove(a1)
if b2==0:
	b1=random.choice(l)
	l.remove(b1)
if c2==0:
	c1=random.choice(l)
	l.remove(c1)
if d2==0:
	d1=random.choice(l)
	l.remove(d1)

if a2==1:
	if b2!=2:
		a1,b1=b1,a1
		a2,b2=b2,a2
	elif c2!=2:
		a1,c1=c1,a1
		a2,c2=c2,a2
	elif d2!=2:
		a1,d1=d1,a1
		a2,d2=d2,a2

if b2==1:
	if b2!=2:
		b1,b1=b1,b1
		b2,b2=b2,b2
	elif c2!=2:
		b1,c1=c1,b1
		b2,c2=c2,b2
	elif d2!=2:
		b1,d1=d1,b1
		b2,d2=d2,b2