def f(t,y):
    return y-t*t+1

def RungeKutta(a,b,y0,n):
    h=(b-a)/n
    import math as mt
    t=a
    y=y0
    z=y0
    x=y0
    lest=[a]
    lesy=[y0]
    lesy4=[y0]
    lesy2=[mt.exp(-a)+a]
    lesyEuler=[y0]
    for i in range(1,n+1):
        #calcule des k
        k1=h*f(t,x)
        k2=h*f(t+h/2,y+k1/2)
        k3=h*f(t+h/2,y+k2/2)
        k4=h*f(t+h,y+k3)
        
        #calcule par raunge Kutta 4  
        x=x+(1/6)*(k1+2*k2+2*k3+k4)
        
        #calcule par raunge Kutta 2
        y=y+h*f(t+(h/2),y+(h/2)*f(t,y))
        
        #calcule par euler
        z=z+h*f(t,z)
        
        #incrémentation du pas
        t=t+h
        
        #soluton exacte
        lesy2.append(mt.exp(-t)+t)
        
        #accumulation des autres méthodes
        lesy.append(y)
        lest.append(t)
        lesyEuler.append(z)
        lesy4.append(x)
    #traçage
    import matplotlib.pyplot as plt 
    plt.plot(lest,lesy,'r',label='Runge Kutta 2')
    #plt.plot(lest,lesy2,label='exacte')
    plt.plot(lest,lesyEuler,'g',label='Euler')
    plt.plot(lest,lesy4,'--',label='Runge Kutta 4')
    plt.legend()
    plt.show()
    #print(lesy4)