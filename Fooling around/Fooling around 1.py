import random

def trans(a,b,c,d):
    return d+10*c+100*b+1000*a

a2,b2,c2,d2=0,0,0,0
l=[0,1,2,3,4,5,6,7,8,9]

while a2*b2*c2*d2==0:
    if a2==0:
        a1=random.choice(l)
        l.remove(a1)
    if b2==0:
        b1=random.choice(l)
        l.remove(b1)
    if c2==0:
        c1=random.choice(l)
        l.remove(c1)
    if d2==0:
        d1=random.choice(l)
        l.remove(d1)
    
    print(str(a1)+str(b1)+str(c1)+str(d1))
    x=input("chban lik ")
    a2=int(x[0])
    b2=int(x[1])
    c2=int(x[2])
    d2=int(x[3])

if a2+b2+c2+d2==8:
    print(trans(a1,b1,c1,d1), "safi salina")
    
elif a2+b2+c2+d2==4:
    b1,c1,d1=d1,b1,c1
    print(str(a1)+str(b1)+str(c1)+str(d1))
    x=int(input("chban lik "))
    if x=="1111":
        b1,c1,d1=c1,d1,b1
        x=input("chban lik ")
        a2=int(x)[0]
        b2=int(x)[1]
        c2=int(x)[2]
        d2=int(x)[3]
    

elif a2+b2+c2+d2==6:
    if a2==2:
        if b2==2:
            c1,d1=d1,c1
            print(trans(a1,b1,c1,d1), "safi salina")
        elif c2==2:
            b1,d1=d1,b1
            print(trans(a1,b1,c1,d1), "safi salina")
        elif d2==2:
            b1,c1=c1,b1
            print(trans(a1,b1,c1,d1), "safi salina")
    elif b2==2:
        if c2==2:
            a1,d1=d1,a1
            print(trans(a1,b1,c1,d1), "safi salina")
        else:
            a1,c1=c1,a1
            print(trans(a1,b1,c1,d1), "safi salina")
    else:
        a1,b1=b1,a1
        print(trans(a1,b1,c1,d1), "safi salina")

elif a2+b2+c2+d2==5:
    if a2==2:
        b1,c1,d1=d1,b1,c1
        print(str(a1)+str(b1)+str(c1)+str(d1))
        x=input("chban lik ")
        if x!="2222":
            b1,c1,d1=c1,d1,b1
            print(trans(a1,b1,c1,d1), "safi salina")
        else:
            print("safi salina")
    elif b2==2:
        a1,c1,d1=d1,a1,c1
        print(str(a1)+str(b1)+str(c1)+str(d1))
        x=input("chban lik ")
        if x!="2222":
            a1,c1,d1=c1,d1,a1
            print(trans(a1,b1,c1,d1), "safi salina")
        else:
            print("safi salina")
    elif c2==2:
        a1,b1,d1=d1,a1,b1
        print(str(a1)+str(b1)+str(c1)+str(d1))
        x=input("chban lik ")
        if x!="2222":
            a1,b1,d1=b1,d1,a1
            print(trans(a1,b1,c1,d1), "safi salina")
        else:
            print("safi salina")
    else:
        a1,b1,c1=c1,a1,b1
        print(str(a1)+str(b1)+str(c1)+str(d1))
        x=input("chban lik ")
        if x!="2222":
            a1,b1,c1=b1,c1,a1
            print(trans(a1,b1,c1,d1), "safi salina")
        else:
            print("safi salina")
    
        

