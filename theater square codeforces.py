n,m,a=[float(k) for k in input().split()]
if int(n/a)==n/a:
	p=n/a
else:
	p=int(n/a)+1
if int(m/a)==m/a:
	q=m/a
else:
	q=int(m/a)+1
print(p*q)


