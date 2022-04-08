import matplotlib.pyplot as plt
import numpy as np
    
#la fonction exacte y = exp(-x^2)
def f(x):
    return np.exp(-x*x)  # x peut être vecteur ou nombre réel 

lesx = np.linspace(0,2,40)#lesx est un vecteur de 40 valeurs

#la courbe de la fonction exacte y = exp(-x^2) 
'''plt.plot(lesx,f(lesx),linewidth=2,label="sol exact") #f(vecteur)---> vecteur 

plt.axis([0,2.05,0,1.02]) 
plt.grid( )
plt.legend()
plt.show()'''

w=20
xf=int(5*w/(2*np.pi))+3
x=np.array([w/(2*np.pi),3*w/(2*np.pi),5*w/(2*np.pi)])
y=np.array([1, 1/3, 1/5])

plt.title("spectre de fourier")
plt.vlines(x,[0,0,0],y)
plt.xlim(0, xf) 
plt.ylim(0, max(y)+1) 
plt.xlabel("fréquence")
plt.ylabel("Amplitude")
plt.show()





