def phi(n):
    if n<=1:
        return 1
    for d in range(2,n+1):
        if n%(d*d)==0:
            print(d,'*phi(',n//d,')')
            return d*phi(n//d)
        elif n%d==0:
            print('(',d,'-1)*phi(',n//d,')')
            return (d-1)*phi(n//d)
n=int(input())
while n!=0:
    print(phi(n))
    n=int(input())