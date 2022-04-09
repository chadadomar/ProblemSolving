a=input()
b=input()
d=int(a)
e=int(b)
c=d+e
c=str(c)
def removeZero(x):
    C=""
    for i in x:
        if i!='0':
            C+=i
    return C
a=int(removeZero(a))
b=int(removeZero(b))
c=int(removeZero(c))
if a+b==c:
    print('YES')
else:
    print('NO')



    