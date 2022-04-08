n=int(input())
for i in range(n):
    c=input()
    if '+' in c:
        l=c.split('+')
        k=int(l[0])+int(l[1])
        print(k)
    else:
        print('skipped')