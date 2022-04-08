#Fonction qui retourn liste des nombre premiers entre 2 et n//2
def ListPremier(n):
    P=[2]
    l=1
    for j in range(2,n//2+1):
        flag=True
        i=0
        while i<l:
            if j%P[i]==0:
                flag=False
                break
            else:
                 i+=1   
        if flag==True:
            P.append(j)
            l+=1
    return P