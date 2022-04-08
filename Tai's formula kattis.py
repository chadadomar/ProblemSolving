n=int(input())
rslt=0
x,y=[float(k) for k in input().split()]
for i in range(n-1):
    z,u=[float(k) for k in input().split()]
    rslt+=(u+y)*(z-x)/2
    x,y=z,u
rslt/=1000
print("%.7f"%rslt)
