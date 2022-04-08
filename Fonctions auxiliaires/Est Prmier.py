import math
#tester si un nombre est premier
def estPremier(n):
    if n==2: return True
    elif n%2==0 : return False
    else:
        f=int(math.sqrt(n))
        for j in range(3,f+1,2):
            if n%j==0:
                return False
        return True