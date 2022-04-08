def valFact(n,p):
    j=p
    s=0
    while j<=n:
        s+=n//j
        j*=p
    return s
    
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
