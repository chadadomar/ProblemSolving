def test(a,b):
    if a//2<=b and b<=2*a:
        return True
    else:
        return False


n=int(input())
l=[int(k) for k in input().split()]
s=[0]*n
for i in range(n-1):
    for j in range(i+1,n):
        if test(l[i],l[j]):
            s[j]=max(s[i]+1,s[j])
print(max(s)+1)