def ListPrime(n):
    if n<3:
        print('entrer une valeur supérieure à 3')
    else:
        tab=[0,0]+[i for i in range(2,n+1)]
        for i in range(1,n-1):
            if tab[i]!=0:
                for j in range(i*i,n+1,i):
                    tab[j]=0
    Prime=[]
    for k in tab:
        if k!=0:
            Prime.append(k)
    return Prime

def cardA(n):
    from math import sqrt
    sum=0
    for y in ListPrime(n):
        sum+=int(sqrt(n*n-y*y))
    return(sum)
    
def Test(n):
    from math import log
    from math import pi
    #print(pi)
    #print(log(1))
    print((log(n)*cardA(n)/(n*n))-pi/8)