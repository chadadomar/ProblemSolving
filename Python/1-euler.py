import matplotlib.pyplot as plt
import numpy as np

#y'=-2xy
def F(y,x):
    return -2*x*y

#méthode d'Euler
def euler(f,y0,x0,xf,N):
    # f : fonction données
    # (y0;x0):point innitial
    # xf : point abscisse final[x0;xf]
    lesy=[y0]#liste des ordonnées yk,k=0;1;2...;N
    lesx=[x0]
    h = (xf-x0)/N #le pas
    for k in range (N):
        y0 += h*F(y0,x0)
        x0 += h
        lesy.append(y0)#stocker les solutions
        lesx.append(x0)#stocker les abscisses
    return lesx,lesy

#la courbe de la fonction y pour n=10
lesxy = euler(f,1,0,2,10) 
lesx,lesy  = lesxy[0],lesxy[1]
plt.plot(lesx,lesy,"--",linewidth=2,label="euler; N=10") 

plt.axis([0,2.05,0,1.02]) 
plt.grid( )
plt.legend()
plt.show()






