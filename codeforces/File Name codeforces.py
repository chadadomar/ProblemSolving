n=int(input())
c=input()
k=0
if n<3:
    print("0")
else:
    for i in range(n-2):
        if c[i]+c[i+1]+c[i+2]=="xxx":
            k+=1
    print(k)