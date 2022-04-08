import math as m

def eratosthene1(n):
    import numpy as np
    a = np.ones(n+1, 'bool')               # n+1 fois True
    a[0] = a[1] = False                    # on barre 0 et 1
    for i in range(2, int(n**0.5)+1):      # de i=2 à sqrt(n)
        if a[i]: a[i*i::i] = False         #     si i non barré, barrer ses suivants
    return np.nonzero(a)[0]                # renvoyer les entiers premiers
    
def eratosthene(n):
    """retourne la tableau des nombres premiers <= n (crible d'eratosthene)"""
    n += 1
    tableau = [0,0] + [i for i in range(2, n)]
    for i in range(2, n):
        if tableau[i] != 0:
            # c'est un nombre 1er: on garde, mais on neutralise ses multiples
            for j in range(i*2, n, i):
                tableau[j] = 0
    return [p for p in tableau if p!=0]
    
def eratosthene2(n):
    """retourne la tableau des nombres premiers <= n (crible d'eratosthene)"""
    n += 1
    tableau = [0,0] + [i for i in range(2, n)]
    for i in range(2,n):
        if tableau[i] != 0:
            # c'est un nombre 1er: on garde, mais on neutralise ses multiples
            for j in range(i*i, n, i):
                tableau[j] = 0
    return [p for p in tableau if p!=0]
