def dichobis(a,b,prec):
    while b-a>prec:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
    return a,b

def f(x):
    return ((1204.816-x)**3)/(233.82**2 + 3*((1204.816-x)**2))-(233.82**4)/3700063.95