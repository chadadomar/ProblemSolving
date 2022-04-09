def divise(n,j):
    x=n/j
    a=0
    while x-int(x)==0:
        a+=1
        x=x/j
    return a
 
"""c=int(input())
n=c//2
k=0
#retourne la tableau des nombres premiers <= n (crible d'eratosthene)
n += 1
tableau = [0,0] + [i for i in range(2, n)]
for i in range(2, n):
    if tableau[i] != 0:
        # c'est un nombre 1er: on garde, mais on neutralise ses multiples
        k+=divise(c,tableau[i])
        for j in range(i*i, n, i):
            tableau[j] = 0
print(k)"""

n=int(input())
k=0
p=3
while 4<=n:
    if n%2==0:
        k+=1
        n//=2

    else:
        break
while p*p<=n:
    if n%p==0:
        k+=1
        n//=p
    else:
        p+=2
print(k+1)