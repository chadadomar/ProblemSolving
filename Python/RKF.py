def f(t,y):
    return -y+t+1
def RKF(a,b,y0,h_max,h_min,Tol):
    import math as mt
    t=a
    w=y0
    h=h_max
    flag=1
    lest=[a]
    lesyRKF=[y0]
    lesy=[y0]
    while flag==1 :
        #Calcule des K
        k1=h*f(t,w)
        k2=h*f(t+h/4,w+k1/4)
        k3=h*f(t+3*h/8,w+3*k1/32+9*k2/32)
        k4=h*f(t+12*h/13,w+1932*k1/2197-7200*k2/2179+7296*k3/2197)
        k5=h*f(t+h,w+439*k1/216-8*k2+3680*k3/513-845*k4/4104)
        k6=h*f(t+h/2,w-8*k1/27+2*k2-3544*k3/2565+1859*k4/4104-11*k5/40)
        
        R=(k1/360-128*k3/4275-2179*k4/75240+k5/50+2*k6/55)/h
        q=0.84*((Tol/R)**1/4)
        if R<=Tol :
            t=t+h
            w=w+25*k1/216+1408*k3/2565+2197*k4/4104-k3/5
            lest.append(t)
            lesyRKF.append(w)
            lesy.append(mt.exp(-t)+t)
        if q <= 0.1:
            h=0.1*h
        else:
            h=q*h
        if h >= h_max :
            h=h_max
        if t>=b :
            flag=0
        elif t+h > b :
            h=b-t
        elif h<=h_min:
            flag=0
            print(0)
    import matplotlib.pyplot as plt
    plt.plot(lest,lesy,label='exacte')
    plt.plot(lest,lesyRKF,'r')
    plt.legend()
    plt.show()
    
    