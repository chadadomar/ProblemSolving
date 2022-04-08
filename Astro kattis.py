d={"1":"Sunday", "2":"Monday", "3":"Tuesday", "4":"Wednesday", "5":"Thursday", "6":"Friday","0":"Saturday"}
def bezout(a, b):
    s, t, u, v = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, s, t, b, u, v = b, u, v, a - q * b, s - q * u, t - q * v
    if a > 0:
        return [a, s, t]
    else:
        return [-a, -s, -t]
l=[]
for i in range(4):
    k=input()
    h=int(k[0]+k[1])
    m=int(k[3]+k[4])
    l.append(h*60+m)
d,u,v=bezout(l[2],l[3])
f=l[1]-l[0]
if f%d!=0:
    print("Never")
else:
    x=abs(u)*l[2]*(f//d)
    y=x//(24*60)
    days=str(y%7)
    print(d[days])
    h=(x-y*24*60)//24
    m=(x-y*24*60-h*60)
    print(h,m)

    