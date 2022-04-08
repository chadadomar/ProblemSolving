import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import  odeint

def F(y,x):
    return -2*x*y


#la fonction odeint
lesx = np.linspace (0,2,40) 
lesy = odeint(F,1,lesx) 
plt.plot(lesx,lesy,linewidth=2,label="fct odeint ")
 #euler
lesxy = euler(f,1,0,2,40)#euler pour N=40  
lesx,lesy  = lesxy[0],lesxy[1]
plt.plot(lesx,lesy,"r:",linewidth=2,label="euler; N=40") 

plt.axis([0,2.05,0,1.02]) 
plt.grid( )
plt.legend()
plt.show()




