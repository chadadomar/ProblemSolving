n=int(input())
s=0
for i in range(n):
    k=int(input())
    num=k//10
    pow=k- num*10
    s+=num**pow
print(s)
