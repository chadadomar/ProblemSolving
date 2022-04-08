from scipy.integrate import  odeint
import numpy as np 
import matplotlib.pyplot as plt   

#y' = -2xy
def F(y,x):
    return -2*x*y

lesx = np.linspace (0,2,40)#40 abcisses entre 0 et 2 
lesy = odeint(F,1,lesx) 
#la courbe de y 
plt.plot(lesx,lesy,linewidth=2,label="fct odeint ") 
plt.show()