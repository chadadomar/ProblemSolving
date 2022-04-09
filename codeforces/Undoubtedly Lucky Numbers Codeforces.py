n=int(input())
if n<=101:
    print(n)
else:
    out=0
    for i in range(1,n+1):
        c=str(i)
        k=len(c)
        l=0
        empty=set()
        for j in range(k):
            #if i>120:
                #print(c[j],' ',end='')
            empty.add(c[j])
        #if i>120 :
            #print('\n')
            #print('this is the set ')
            #for x in empty:
                #print(x,',',end='')
        if len(empty)<=2:
            out+=1
        #else:
            #print(i)
        #if i>120:
            #print('\n')
    print(out)