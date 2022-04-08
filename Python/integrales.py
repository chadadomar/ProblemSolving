def R():
    from math import pi
    from math import cos
    r=pi/2
    s=0
    for k in range(2,20):
        for i in range(1,2**(k-2)+1):
            s+=cos((i-0.5)*pi/2**(k-1))
        r=r+(pi/2**(k-1))*s
        r=r/2
    print(r)
    