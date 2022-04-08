O=['?',0,'?']
def inv(K):
    for i in range(len(K)//2):
        K[i],K[len(K)-i-1]=K[len(K)-i-1],K[i]
    return K
def j(x,n):                 #écriture en binaire
    l=[]
    if x>2**n: return False
    else:
        for i in range(1,n+1):
            if x>=2**(n-i):
                l.append(x//2**(n-i))
                x=x%2**(n-i)
            else:
                l.append(0)
        return inv(l)
def gen(n):                 #générateur de liste de 0s and 1s
    L=[]
    for i in range(2**n):
        L.append(j(i,n))
    return L
def indx(L):                #les positions des '?'
    ind=[]
    for i in range(len(L)):
        if L[i]=='?':
            ind.append(i)
    return ind
def replace(O,C):           #replace les '?' avec les 0s et 1s
    L=[]
    for i in O:             #pourquoi n'ecrire l=O?
        L.append(i)
    for i in range(len(C)):
        L[indx(O)[i]]=C[i]
    return L
def tritest(M):               #tester si la liste est triée?
    if len(M)==2:
        if M[0]==1 and M[1]==0:
            return False
        else: return True
    else:
        for i in range(1,len(M)-1):
            if M[i-1]>M[i] or M[i+1]<M[i]:   #pourquoi 2 comp?
                return False
        return True
def tri(M):        #trier la liste générés et return le nb d'inversions.
    no=0
    if M==[1]*len(M) or M==[0]*len(M):
        return 0    
    else:
        while tritest(M)==False:
            for i in range(len(M)-1):
                if M[i]==1 and M[i+1]==0:
                    M[i],M[i+1]=M[i+1],M[i]
                    no+=1
    return no

        
        
def OmarNbOfInv(L):
    k=len(L)
    index=sum=0
    for i in range(k):
        if L[i]==0:
            sum+=i-index
            index+=1
    return sum
    
    
    
    
def fin(K):
    C=gen(len(indx(K)))
    nt=0
    for i in range(2**len(indx(K))):
        #nt+=tri(replace(K,C[i]))
        nt+=OmarNbOfInv(replace(K,C[i]))
    return nt
                        
            
                    
    
            
        

