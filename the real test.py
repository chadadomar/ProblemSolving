def Nv(L):
    sum=index=0
    if len(L)==0:
        return 0
    else:    
        for i in range(len(L)):
            if L[i]==0:
                sum+=i-index
                index+=1
        return sum
        
        
def clear(l):
    grp=[]
    h=[]
    M=[]
    for i in range(len(l)):
        if l[i]!='?':
            h.append(l[i])
        else:
             M.append(i)
    grp.append(h)
    grp.append(M)
    return grp
            

def nomf(l):
    grp=clear(l)
    N=grp[0]
    M=grp[1]
    n=len(M)
    sum=0
    temp=0
    sum+=(2**n)*Nv(N)+(2**(n-2))*n*(n-1)//2+(2**(n-1))*(n+1)*l[:M[-1]].count(1)
    temp+=l[M[0]+1:M[1]].count(0)-l[:M[0]].count(1)+n*(l[M[-1]:].count(0)-l[M[-2]+1:M[-1]].count(1))
    for i in range(1,n-1):
        temp+=(i+1)*(l[M[i]+1:M[i+1]].count(0)-l[M[i-1]+1:M[i]].count(1))
    sum+=temp*(2**(n-1))
    return int(sum)

"""c=input()
l=[]
for e in c:
    if e=='?':
        l.append(e)
    else:
        l.append(int(e))

print(nomf(l))"""







"""def NombreInv(L):
    import time
    temp1=time.clock()
    Ninv=0
    M=PositionDeVide(L)
    l=len(M)
    n1g=L[:M[0]].count(1)
    #print('9bal lboucle a sat n1g :',n1g)
    n0d=L[M[0]+1:M[1]].count(0)
    #print('9bal lboucle a sat n0d :',n0d)
    Ninv+= 2*(Nv(L[:M[0]])+Nv(L[M[0]+1:M[1]]))+2*n1g*n0d+n1g+n0d
    #print('9bal lboucle a sat Ninv :',Ninv)
    for k in range(1,l-1):
        n1g+=L[M[k-1]+1:M[k]].count(1)
        #print('hna db wast boucle a sat n1g :',n1g)
        n0d=L[M[k]+1:M[k+1]].count(0)
        #print('hna db wast boucle a sat n0d :',n0d)
        Ninv=2*(Ninv+Nv(L[M[k]+1:M[k+1]]))+2**k*(2*n1g*n0d+n1g+n0d)+2**(k-1)*(2*n0d+1)
        #print('hna db wast boucle a sat Ninv :',Ninv)
 
    n1g+=L[M[l-2]+1:M[l-1]].count(1)
    #print('hna db wast condition a sat n1g :',n1g)
    n0d=L[M[l-1]:].count(0)
    #print('hna db wast cndition a sat n0d :',n0d)
    Ninv=2*(Ninv+Nv(L[M[l-1]+1:]))   +(2**(l-1))*   (    2*n1g*n0d+n1g+n0d ) +  2**(l-2)* (l-1)*(2*n0d+1)
    #print('hna db wast condition a sat Ninv :',Ninv)
    temp2=time.clock()
    #print(temp2-temp1)
    return Ninv%1000000007"""